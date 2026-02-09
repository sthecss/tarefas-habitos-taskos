import csv
import os
from src.dominio.models import Habito

ARQUIVO_CADERNINHO = 'data/caderninho.csv'


def _inicializar():
    if not os.path.exists('data'): os.makedirs('data')
    if not os.path.exists(ARQUIVO_CADERNINHO):
        with open(ARQUIVO_CADERNINHO, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(['id', 'nome', 'frequencia', 'contador'])


def listar_arquivados() -> list[Habito]:
    _inicializar()
    habitos = []
    with open(ARQUIVO_CADERNINHO, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                habitos.append(Habito(
                    id=int(row['id']),
                    nome=row['nome'],
                    frequencia=row['frequencia'],
                    contador_execucoes=int(row['contador'])
                ))
            except:
                continue
    return habitos


def arquivar(habito: Habito):
    _inicializar()
    atuais = listar_arquivados()
    if any(h.id == habito.id for h in atuais):
        return

    with open(ARQUIVO_CADERNINHO, 'a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow([habito.id, habito.nome, habito.frequencia, habito.contador_execucoes])


def desarquivar(id_habito: int) -> Habito:
    habitos = listar_arquivados()
    recuperado = None
    novos = []

    for h in habitos:
        if h.id == id_habito:
            recuperado = h
        else:
            novos.append(h)

    with open(ARQUIVO_CADERNINHO, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nome', 'frequencia', 'contador'])
        for h in novos:
            writer.writerow([h.id, h.nome, h.frequencia, h.contador_execucoes])

    return recuperado