# Projeto D – Gerenciador de Tarefas e Hábitos 

## Taskos 🧙‍♂️📋

**Taskos** é um gerenciador de tarefas e hábitos gamificado, desenvolvido em Python, que utiliza conceitos de RPG (XP, níveis e progressão) para incentivar constância e organização pessoal.

O projeto foi estruturado seguindo os princípios da **Clean Architecture**, mantendo regras de negócio independentes de framework, interface ou persistência.

Funcionalidades

    [x] CRUD de Tarefas (A Fazer, Fazendo, Concluído)

    [x] Gerenciamento de Hábitos com Frequência

    [x] Sistema de Ganho de XP e Level Up

    [x] Lixeira com Restauração

    [x] Efeitos Sonoros para interações

---

## Tecnologias

- **Python** 3.10+
- **FastAPI**
- **Uvicorn**
- **Jinja2**
- **CSS3**
- **Persistência:** CSV
- **Arquitetura:** Clean Architecture

---

## Estrutura do Projeto

```text
Taskos_Tarefas_Habitos/
│
├── .venv/                      # Ambiente virtual Python
│
├── data/                       # Persistência local (CSV e TXT)
│   ├── caderninho.csv
│   ├── habitos.csv
│   ├── lixeira.csv
│   ├── tarefas.csv
│   └── usuario.txt
│
├── src/                        # Código-fonte principal
│   ├── aplicacao/              # Lógica de aplicação e relatórios
│   │   ├── __init__.py
│   │   └── relatorios.py
│   │
│   ├── dominio/                # Núcleo do sistema (entidades)
│   │   ├── __init__.py
│   │   └── models.py
│   │
│   ├── infraestrutura/         # Repositórios e acesso a dados
│   │   ├── __init__.py
│   │   ├── repositorio_habitos.py
│   │   ├── repositorio_tarefas.py
│   │   └── outros repositórios
│   │
│   └── server.py               # Ponto de entrada da aplicação (FastAPI)
│
├── static/                     # Arquivos estáticos (frontend)
│   ├── audio/                  # Efeitos sonoros
│   ├── css/                    # Estilos visuais
│   ├── img/                    # Imagens e elementos gráficos
│   └── js/                     # Scripts JavaScript
│
├── templates/                  # Templates HTML (Jinja2)
│   └── index.html
│
├── .gitignore                  # Arquivos ignorados pelo Git
├── README.md                   # Documentação do projeto
└── requirements.txt            # Dependências Python
````

---
<br><br>

## Instalação (primeira vez)

### 1. Clone o repositório

```bash
git clone https://github.com/sthecss/tarefas-habitos-taskos.git
cd tarefas-habitos-taskos
```

---
<br>

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
```

---
<br>

### 3. Ative o ambiente virtual

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

Se aparecer `(.venv)` no terminal, deu certo.

---
<br>

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---
<br><br>

## Como rodar o projeto

### Primeira execução ou sempre que abrir um novo terminal

1. Entre na pasta do projeto

```bash
cd tarefas-habitos-taskos
```

2. Ative o ambiente virtual

```bash
source .venv/bin/activate
```

3. Inicie o servidor

```bash
python -m src.server
```

---
<br>

### Acesse no navegador

```
http://127.0.0.1:8000
```

---
<br><br>

## Dica para rodar mais rápido (opcional)

Crie um script para automatizar:

### `run.sh` (Linux / macOS)

```bash
#!/bin/bash
source .venv/bin/activate
python -m src.server
```

<br>
Dê permissão:

```bash
chmod +x run.sh
```

Depois disso, basta rodar:

```bash
./run.sh
```

---
<br><br>

## Observações

* O servidor utiliza **FastAPI + Uvicorn**
* Os dados são persistidos localmente em arquivos CSV
* A aplicação não depende de banco de dados externo
* Ideal para estudo de arquitetura e projetos modulares em Python

---
<br><br>

## Possíveis Evoluções

* Persistência com banco de dados
* Sistema de conquistas
* Perfis de usuário
* Estatísticas avançadas
* Temas visuais desbloqueáveis

---
<br><br>

````
  Desenvolvido por Sthe.
````

