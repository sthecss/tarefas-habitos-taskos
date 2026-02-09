import csv
import os
from src.dominio.models import Habito

ARQUIVO_DADOS = 'data/habitos.csv'


def _inicializar_arquivo():
    if not os.path.exists('data'): os.makedirs('data')

    precisa_migrar = False
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            if 'xp' not in f.readline().strip():
                precisa_migrar = True

    if not os.path.exists(ARQUIVO_DADOS) or precisa_migrar:
        if not os.path.exists(ARQUIVO_DADOS):
            with open(ARQUIVO_DADOS, 'w', newline='', encoding='utf-8') as f:
                csv.writer(f).writerow(['id', 'nome', 'frequencia', 'contador', 'xp'])


def listar_todos() -> list[Habito]:
    _inicializar_arquivo()
    habitos = []
    with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                xp_val = int(row.get('xp', 10))
                h = Habito(
                    id=int(row['id']),
                    nome=row['nome'],
                    frequencia=row['frequencia'],
                    contador_execucoes=int(row['contador'])
                )
                h.xp = xp_val
                habitos.append(h)
            except:
                continue
    return habitos


def adicionar(habito: Habito):
    _inicializar_arquivo()
    lista = listar_todos()
    novo_id = 1
    if lista:
        novo_id = max(h.id for h in lista) + 1
    habito.id = novo_id

    if not hasattr(habito, 'xp'): habito.xp = 10  # Default

    with open(ARQUIVO_DADOS, 'a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow([habito.id, habito.nome, habito.frequencia, habito.contador_execucoes, habito.xp])


def atualizar(id_habito: int, nome: str, frequencia: str, xp: int):
    habitos = listar_todos()
    for h in habitos:
        if h.id == id_habito:
            h.nome = nome
            h.frequencia = frequencia
            h.xp = xp
            break

    _reescrever_arquivo(habitos)

def incrementar_execucao(id_habito: int):
    habitos = listar_todos()
    for h in habitos:
        if h.id == id_habito:
            h.registrar_execucao()
            break
    _reescrever_arquivo(habitos)


def excluir(id_habito: int):
    habitos = listar_todos()
    removido = None
    novos = []
    for h in habitos:
        if h.id == id_habito:
            removido = h
        else:
            novos.append(h)
    if removido:
        _reescrever_arquivo(novos)
    return removido


def _reescrever_arquivo(habitos: list[Habito]):
    with open(ARQUIVO_DADOS, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nome', 'frequencia', 'contador', 'xp'])
        for h in habitos:
            xp = getattr(h, 'xp', 10)
            writer.writerow([h.id, h.nome, h.frequencia, h.contador_execucoes, xp])