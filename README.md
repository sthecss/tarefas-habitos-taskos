# Projeto D – Gerenciador de Tarefas e Hábitos 

## Taskos 🧙‍♂️📋

**Taskos** é um gerenciador de tarefas e hábitos gamificado, desenvolvido em Python, que utiliza conceitos de RPG (XP, níveis e progressão) para incentivar constância e organização pessoal.

O projeto foi estruturado seguindo os princípios da **Clean Architecture**, mantendo regras de negócio independentes de framework, interface ou persistência.

<br>

### Funcionalidades

    [x] CRUD de Tarefas (A Fazer, Fazendo, Concluído)

    [x] Gerenciamento de Hábitos com Frequência

    [x] Sistema de Ganho de XP e Level Up

    [x] Lixeira com Restauração

    [x] Efeitos Sonoros para interações

---
<br>

## Tecnologias

- **Python** 3.10+
- **FastAPI**
- **Uvicorn**
- **Jinja2**
- **CSS3**
- **Persistência:** CSV
- **Arquitetura:** Clean Architecture

---
<br>

## Estrutura do Projeto
<details>
<summary><strong>Checar</strong></summary>

```text
Taskos_Tarefas_Habitos/
│
├── .venv/
├── data/
│   ├── caderninho.csv
│   ├── habitos.csv
│   ├── lixeira.csv
│   ├── tarefas.csv
│   └── usuario.txt
│
├── src/
│   ├── aplicacao/
│   ├── dominio/
│   ├── infraestrutura/
│   └── server.py
│
├── static/
├── templates/
├── .gitignore
├── README.md
└── requirements.txt
````

</details>

---
<br>

### Como baixar: 

<details>
<summary><strong>Instalação</strong></summary>

### 1. Clone o repositório
```bash
git clone https://github.com/sthecss/tarefas-habitos-taskos.git
cd tarefas-habitos-taskos
````

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

</details>  

<br>

<details>
<summary><strong>Como rodar</strong></summary>

Primeira execução ou sempre que abrir um novo terminal

```bash
cd tarefas-habitos-taskos
source .venv/bin/activate
python -m src.server
````

Acesse:

```
http://127.0.0.1:8000
```

</details>

<br>

<details>
<summary><strong>Dica para rodar mais rápido (run.sh)</strong></summary>

```bash
#!/bin/bash
source .venv/bin/activate
python -m src.server
````

```bash
chmod +x run.sh
./run.sh
```

</details>

---
<br>

### Observações

* O servidor utiliza FastAPI + Uvicorn 
* Os dados são persistidos localmente em arquivos CSV 
* A aplicação não depende de banco de dados externo 
* Ideal para estudo de arquitetura e projetos modulares em Python

---
<br>

### Possíveis Evoluções

- Persistência com banco de dados
- Sistema de conquistas
- Perfis de usuário
- Estatísticas avançadas
- Temas visuais desbloqueáveis

