# Taskos 🧙‍♂️📋

**Taskos** é um gerenciador de tarefas e hábitos gamificado, criado para transformar a rotina em algo menos mecânico e mais… jogável.

Aqui, produtividade não é cobrança.  
É **progressão**.

---

## A Ideia por Trás do Projeto

O Taskos nasceu da frustração com ferramentas de produtividade que tratam pessoas como máquinas de checklist.

A proposta é simples:
> se a vida exige constância, então constância merece recompensa.

Em vez de punições por falhar um dia, o sistema incentiva retomadas, continuidade e senso de avanço.  
Você não “atrasou tarefas”. Você só está em *grindando*.

---

## Arquitetura do Projeto

O projeto segue os princípios da **Arquitetura Limpa (Clean Architecture)**, garantindo separação clara de responsabilidades e facilidade de evolução futura.

### Camadas

- **Domínio (`src/dominio`)**  
  Contém as entidades centrais do sistema, como `Tarefa` e `Habito`.  
  É o coração do projeto e não depende de nenhuma tecnologia externa.

- **Infraestrutura (`src/infraestrutura`)**  
  Responsável pela persistência de dados.  
  Atualmente utiliza **arquivos CSV**, mas pode ser substituída facilmente por um banco SQL ou NoSQL no futuro.

- **Aplicação (`src/aplicacao`)**  
  Onde vivem as regras de negócio, cálculos de XP, relatórios e orquestração entre domínio e infraestrutura.

- **Interface Web (`src/server.py` e `templates`)**  
  Camada externa, construída com **FastAPI** e **Jinja2**, responsável pela comunicação com o usuário via navegador.

---

## Funcionalidades

- **Quadro Kanban**  
  Tarefas organizadas em *A Fazer*, *Em Progresso* e *Histórico*.

- **Sistema de XP e Níveis**  
  Cada ação rende experiência.  
  A cada 100 XP, o usuário sobe de nível.

- **Caderninho de Hábitos**  
  Hábitos antigos podem ser arquivados para manter a interface limpa, sem perder histórico.

- **Lixeira com Restauração**  
  Exclusões não são definitivas. Recuperação é possível.

---

## Tecnologias Utilizadas

- **Linguagem**: Python 3.14+
- **Framework Web**: FastAPI
- **Template Engine**: Jinja2
- **Persistência**: CSV
- **Estilização**: CSS moderno com variáveis e Grid Layout

---

## Como Executar Localmente

1. Clone o repositório:
```bash
git clone https://github.com/sthecss/tarefas-habitos-taskos.git
cd tarefas-habitos-taskos
````

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie o servidor:

```bash

```

4. Acesse no navegador:

```
http://127.0.0.1:8000
```

---

## Possíveis Evoluções

* Persistência com banco de dados
* Sistema de conquistas
* Perfis de usuário
* Estatísticas avançadas de hábitos
* Temas visuais desbloqueáveis por nível

