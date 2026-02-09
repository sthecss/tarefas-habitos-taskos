import os

# caminho do arquivo onde o nome fica salvo
ARQUIVO_USUARIO = 'data/usuario.txt'


def _inicializar():
    """garante que a pasta 'data' e o arquivo existam."""
    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.exists(ARQUIVO_USUARIO):
        with open(ARQUIVO_USUARIO, 'w', encoding='utf-8') as f:
            f.write("Viajante")


def obter_nome() -> str:
    """lê o nome do arquivo."""
    _inicializar()
    try:
        with open(ARQUIVO_USUARIO, 'r', encoding='utf-8') as f:
            nome = f.read().strip()
            return nome if nome else "Viajante"
    except Exception as e:
        print(f"Erro ao ler nome: {e}")
        return "Viajante"


def salvar_nome(novo_nome: str):
    """salva o novo nome no arquivo."""
    _inicializar()
    try:
        nome_limpo = novo_nome.strip()
        if not nome_limpo:
            return

        with open(ARQUIVO_USUARIO, 'w', encoding='utf-8') as f:
            f.write(nome_limpo)
    except Exception as e:
        print(f"Erro ao salvar nome: {e}")