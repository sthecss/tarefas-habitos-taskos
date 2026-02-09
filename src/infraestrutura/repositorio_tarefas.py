import csv
import os
from src.dominio.models import Tarefa

ARQUIVO_DADOS = 'data/tarefas.csv'


def _inicializar_arquivo():
    if not os.path.exists('data'):
        os.makedirs('data')

    precisa_migrar = False
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            cabecalho = f.readline().strip()
            if 'xp' not in cabecalho:
                precisa_migrar = True

    if not os.path.exists(ARQUIVO_DADOS) or precisa_migrar:
        with open(ARQUIVO_DADOS, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(['id', 'titulo', 'descricao', 'data_limite', 'status', 'xp'])


def listar_todos() -> list[Tarefa]:
    _inicializar_arquivo()
    tarefas = []
    with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                t = Tarefa(
                    id=int(row['id']),
                    titulo=row['titulo'],
                    descricao=row.get('descricao', ''),
                    data_limite=row['data_limite'],
                    status=row.get('status', 'pendente'),
                    xp=int(row.get('xp', 50))
                )
                t.concluida = (t.status == 'concluida')
                tarefas.append(t)
            except:
                continue
    return tarefas


def adicionar(tarefa: Tarefa):
    _inicializar_arquivo()
    lista = listar_todos()
    novo_id = 1
    if lista:
        novo_id = max(t.id for t in lista) + 1

    tarefa.id = novo_id
    if not tarefa.status: tarefa.status = 'pendente'
    if not tarefa.xp: tarefa.xp = 50

    lista.append(tarefa)
    _reescrever_arquivo(lista)


def atualizar(id_tarefa: int, titulo: str, descricao: str, data_limite: str, xp: int):
    lista = listar_todos()
    for t in lista:
        if t.id == id_tarefa:
            t.titulo = titulo
            t.descricao = descricao
            t.data_limite = data_limite
            t.xp = xp
            break
    _reescrever_arquivo(lista)


def mover_status(id_tarefa: int, novo_status: str):
    lista = listar_todos()
    for t in lista:
        if t.id == id_tarefa:
            t.status = novo_status
            break
    _reescrever_arquivo(lista)


def excluir(id_tarefa: int):
    lista = listar_todos()
    removido = None
    nova_lista = []
    for t in lista:
        if t.id == id_tarefa:
            removido = t
        else:
            nova_lista.append(t)

    if removido:
        _reescrever_arquivo(nova_lista)
    return removido


def _reescrever_arquivo(tarefas: list[Tarefa]):
    with open(ARQUIVO_DADOS, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'titulo', 'descricao', 'data_limite', 'status', 'xp'])
        for t in tarefas:
            writer.writerow([t.id, t.titulo, t.descricao, t.data_limite, t.status, t.xp])