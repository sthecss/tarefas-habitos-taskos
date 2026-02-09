import csv
import os
from datetime import datetime

ARQUIVO_LIXEIRA = 'data/lixeira.csv'


def _inicializar():
    if not os.path.exists('data'): os.makedirs('data')
    if not os.path.exists(ARQUIVO_LIXEIRA):
        with open(ARQUIVO_LIXEIRA, 'w', newline='', encoding='utf-8') as f:
            # id_orig: ID que tinha antes de apagar
            # dados_json: string com titulo|desc|data ou nome|freq|count
            csv.writer(f).writerow(['id_orig', 'tipo', 'dados_extra', 'data_exclusao'])


def arquivar_item(id_orig, tipo, dados_extra: str):
    _inicializar()
    data_hora = datetime.now().strftime("%d/%m %H:%M")
    with open(ARQUIVO_LIXEIRA, 'a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow([id_orig, tipo, dados_extra, data_hora])


def listar_paginado(pagina=1, itens_por_pagina=5):
    _inicializar()
    itens = []
    with open(ARQUIVO_LIXEIRA, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            itens.append(row)

    itens.reverse()

    total_items = len(itens)
    import math
    total_paginas = math.ceil(total_items / itens_por_pagina)

    inicio = (pagina - 1) * itens_por_pagina
    fim = inicio + itens_por_pagina
    return itens[inicio:fim], total_paginas


def recuperar_e_remover(indice_na_lista_reversa: int):
    """
    remove o item da lixeira e retorna seus dados.
    nota: o índice vem da visualização (que está invertida).
    """
    _inicializar()
    itens = []
    with open(ARQUIVO_LIXEIRA, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            itens.append(row)

    indice_real = len(itens) - 1 - indice_na_lista_reversa

    if 0 <= indice_real < len(itens):
        item_recuperado = itens.pop(indice_real)

        # reescreve o arquivo sem esse item
        with open(ARQUIVO_LIXEIRA, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id_orig', 'tipo', 'dados_extra', 'data_exclusao'])
            for item in itens:
                writer.writerow([item['id_orig'], item['tipo'], item['dados_extra'], item['data_exclusao']])

        return item_recuperado
    return None

def limpar_tudo():
    """
    esvazia completamente a lixeira, mantendo apenas o cabeçalho do CSV.
    """
    _inicializar()
    # abre no modo 'w' (write) que sobrescreve tudo
    with open(ARQUIVO_LIXEIRA, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # reescreve apenas o cabeçalho padrão
        writer.writerow(['id_orig', 'tipo', 'dados_extra', 'data_exclusao'])