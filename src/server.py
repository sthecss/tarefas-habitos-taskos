from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import math
import os

from src.dominio.models import Tarefa, Habito
import src.infraestrutura.repositorio_tarefas as repo_tarefas
import src.infraestrutura.repositorio_habitos as repo_habitos
import src.infraestrutura.repositorio_usuario as repo_usuario
import src.infraestrutura.repositorio_lixeira as repo_lixeira
import src.infraestrutura.repositorio_caderninho as repo_caderninho

app = FastAPI()
if not os.path.exists("static"): os.makedirs("static")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request, page_task: int = 1, page_hab: int = 1, page_hist: int = 1, page_lix: int = 1):
    nome_usuario = repo_usuario.obter_nome()
    tarefas = repo_tarefas.listar_todos()
    habitos = repo_habitos.listar_todos()
    caderninho_itens = repo_caderninho.listar_arquivados()

    pendentes = [t for t in tarefas if getattr(t, 'status', 'pendente') == 'pendente']
    fazendo = [t for t in tarefas if getattr(t, 'status', 'pendente') == 'progresso']
    concluidas = [t for t in tarefas if getattr(t, 'status', 'pendente') == 'concluida']
    concluidas.reverse()

    xp_tarefas = sum(getattr(t, 'xp', 50) for t in concluidas)

    xp_habitos = sum(h.contador_execucoes * getattr(h, 'xp', 10) for h in habitos)

    xp_caderninho = sum(h.contador_execucoes * 10 for h in caderninho_itens)

    total_xp = xp_tarefas + xp_habitos + xp_caderninho
    nivel = int(total_xp // 100) + 1
    progresso_nivel = total_xp % 100

    def paginar(lista, pagina, itens_por_pag):
        total = len(lista)
        total_pg = math.ceil(total / itens_por_pag)
        if pagina < 1: pagina = 1
        if pagina > total_pg and total_pg > 0: pagina = total_pg
        inicio = (pagina - 1) * itens_por_pag
        return lista[inicio:inicio + itens_por_pag], pagina, total_pg

    pendentes_pag, page_task, total_pg_task = paginar(pendentes, page_task, 6)
    habitos_pag, page_hab, total_pg_hab = paginar(habitos, page_hab, 4)
    hist_pag, page_hist, total_pg_hist = paginar(concluidas, page_hist, 6)
    lix_pag, total_pg_lix = repo_lixeira.listar_paginado(page_lix, 6)

    stats = {
        "tarefas_concluidas": len(concluidas),
        "habitos_ativos": len(habitos),
        "total_xp": total_xp,
        "nivel": nivel,
        "progresso": progresso_nivel
    }

    return templates.TemplateResponse("index.html", {
        "request": request, "usuario": nome_usuario, "stats": stats,
        "pendentes": pendentes_pag, "fazendo": fazendo,
        "habitos": habitos_pag, "historico": hist_pag,
        "lixeira": lix_pag, "caderninho": caderninho_itens,
        "pg_task": {"atual": page_task, "total": total_pg_task},
        "pg_hab": {"atual": page_hab, "total": total_pg_hab},
        "pg_hist": {"atual": page_hist, "total": total_pg_hist},
        "pg_lix": {"atual": page_lix, "total": total_pg_lix}
    })


@app.post("/tarefa/nova")
async def criar_tarefa(titulo: str = Form(...), descricao: str = Form(""), data_limite: str = Form(...),
                       xp: int = Form(50)):
    nova = Tarefa(0, titulo, descricao, data_limite)
    nova.status = 'pendente'
    nova.xp = xp
    repo_tarefas.adicionar(nova)
    return RedirectResponse(url="/", status_code=303)


@app.post("/tarefa/editar")
async def editar_tarefa(id_tarefa: int = Form(...), titulo: str = Form(...), descricao: str = Form(""),
                        data_limite: str = Form(...), xp: int = Form(50)):
    repo_tarefas.atualizar(id_tarefa, titulo, descricao, data_limite, xp)
    return RedirectResponse(url="/", status_code=303)


@app.post("/tarefa/mover/{id}/{status}")
async def mover_tarefa(id: int, status: str):
    repo_tarefas.mover_status(id, status)
    return RedirectResponse(url="/", status_code=303)


@app.post("/tarefa/concluir/{id}")
async def concluir_tarefa(id: int):
    repo_tarefas.mover_status(id, 'concluida')
    return RedirectResponse(url="/", status_code=303)


@app.post("/tarefa/excluir/{id}")
async def excluir_tarefa(id: int):
    t = repo_tarefas.excluir(id)
    if t:
        xp = getattr(t, 'xp', 50)
        repo_lixeira.arquivar_item(t.id, "tarefa", f"{t.titulo}|{t.descricao}|{t.data_limite}|{xp}")
    return RedirectResponse(url="/", status_code=303)


@app.post("/habito/novo")
async def criar_habito(nome: str = Form(...), tipo: str = Form("Diario"), xp: int = Form(10)):
    h = Habito(0, nome, tipo)
    h.xp = xp
    repo_habitos.adicionar(h)
    return RedirectResponse(url="/", status_code=303)


@app.post("/habito/editar")
async def editar_habito(
    id_habito: int = Form(...),
    nome: str = Form(...),
    tipo: str = Form(...),
    xp: int = Form(...)
):
    repo_habitos.atualizar(id_habito, nome, tipo, xp)
    return RedirectResponse(url="/", status_code=303)

@app.post("/habito/check/{id}")
async def check_habito(id: int):
    repo_habitos.incrementar_execucao(id)
    return RedirectResponse(url="/", status_code=303)


@app.post("/habito/excluir/{id}")
async def excluir_habito(id: int):
    h = repo_habitos.excluir(id)
    if h:
        xp = getattr(h, 'xp', 10)
        repo_lixeira.arquivar_item(h.id, "habito", f"{h.nome}|{h.frequencia}|{h.contador_execucoes}|{xp}")
    return RedirectResponse(url="/", status_code=303)


@app.post("/habito/arquivar/{id}")
async def arquivar_habito(id: int):
    h = repo_habitos.excluir(id)
    if h: repo_caderninho.arquivar(h)
    return RedirectResponse(url="/", status_code=303)


@app.post("/habito/restaurar/{id}")
async def restaurar_habito(id: int):
    h = repo_caderninho.desarquivar(id)
    if h: repo_habitos.adicionar(h)
    return RedirectResponse(url="/", status_code=303)


@app.post("/lixeira/restaurar/{idx}/{page}")
async def restaurar_lixeira(idx: int, page: int):
    item = repo_lixeira.recuperar_e_remover(((page - 1) * 6) + idx)
    if item:
        dados = item['dados_extra'].split('|')
        tipo = item['tipo']
        if tipo == 'tarefa':
            xp = int(dados[3]) if len(dados) > 3 else 50
            t = Tarefa(0, dados[0], dados[1], dados[2])
            t.status = 'pendente'
            t.xp = xp
            repo_tarefas.adicionar(t)
        elif tipo == 'habito':
            xp = int(dados[3]) if len(dados) > 3 else 10
            h = Habito(0, dados[0], dados[1], int(dados[2]))
            h.xp = xp
            repo_habitos.adicionar(h)
    return RedirectResponse(url=f"/?page_lix={page}", status_code=303)


@app.post("/lixeira/limpar")
async def limpar_lixeira_geral(request: Request):
    repo_lixeira.limpar_tudo()
    params = request.query_params
    return RedirectResponse(
        url=f"/?page_task={params.get('page_task', 1)}&page_hab={params.get('page_hab', 1)}&page_lix=1",
        status_code=303)


@app.post("/usuario/alterar")
async def alterar_nome(nome: str = Form(...)):
    repo_usuario.salvar_nome(nome)
    return RedirectResponse(url="/", status_code=303)


@app.post("/sistema/resetar")
async def resetar():
    import csv

    cabecalhos = { # Atualiza cabeçalhos para incluir XP
        'tarefas.csv': ['id', 'titulo', 'descricao', 'data_limite', 'status', 'xp'],
        'habitos.csv': ['id', 'nome', 'frequencia', 'contador', 'xp'],
        'lixeira.csv': ['id_orig', 'tipo', 'dados_extra', 'data_exclusao'],
        'caderninho.csv': ['id', 'nome', 'frequencia', 'contador']
    }
    for arq, cols in cabecalhos.items():
        with open(f'data/{arq}', 'w', newline='', encoding='utf-8') as f: csv.writer(f).writerow(cols)
    with open('data/usuario.txt', 'w', encoding='utf-8') as f: f.write("Viajante")
    return RedirectResponse(url="/", status_code=303)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)