<<<<<<< HEAD
# Taskos

O **Taskos** é um gerenciador de tarefas e hábitos gamificado, desenvolvido para transformar a produtividade diária em uma experiência de RPG. O sistema recompensa o usuário com **XP** ao concluir tarefas e manter sequências (*streaks*) de hábitos, permitindo a progressão de níveis.

## Arquitetura do Projeto

O projeto foi construído seguindo os princípios da **Arquitetura Limpa (Clean Architecture)**, separando as responsabilidades em camadas distintas para garantir que a lógica de negócio seja independente de tecnologias externas (como o framework web ou o banco de dados).

* **Domínio (`src/dominio`)**: Contém as entidades principais do sistema (`Tarefa` e `Habito`). Esta camada é o coração do projeto e não depende de nenhuma outra.  
<br>
* **Infraestrutura (`src/infraestrutura`)**: Responsável pela persistência dos dados. Aqui, implementamos repositórios que gerenciam a leitura e escrita em arquivos **CSV**, garantindo que, se no futuro quisermos usar um banco de dados SQL, bastaria trocar esta camada.  
<br>
* **Aplicação (`src/aplicacao`)**: Contém a lógica de relatórios e regras de negócio específicas que orquestram os dados.  
<br>
* **Interface Web (`src/server.py` & `templates`)**: Utiliza **FastAPI** e **Jinja2** para servir a interface ao usuário. É a camada mais externa que se comunica com o navegador.  

## Funcionalidades

* **Quadro Kanban**: Divisão de tarefas entre *A Fazer*, *Em Progresso* e *Histórico* (com as concluídas).
* **Sistema de XP**: Cada tarefa e hábito possui um valor de experiência. Ao acumular 100 XP, o usuário sobe de nível.
* **Caderninho de Hábitos**: Permite arquivar hábitos antigos para manter a interface limpa, sem perder o histórico de execuções.
* **Lixeira com Restauração**: Itens excluídos podem ser recuperados, evitando perdas acidentais de dados.

## 🚀 Tecnologias Utilizadas

* **Linguagem**: Python 3.14+
* **Framework Web**: FastAPI
* **Template Engine**: Jinja2
* **Persistência**: CSV (Comma-Separated Values)
* **Estilização**: CSS Moderno com variáveis e Grid Layout

## 🛠️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/taskos.git

```


2. Instale as dependências:
```bash
pip install -r requirements.txt

```


3. Inicie o servidor:
```bash
python main.py

```


4. Acesse em seu navegador: `http://127.0.0.1:8000`

---

### Dica de Ouro para o GitHub:

No seu GitHub, você pode ir em **Settings -> Pages** e, se estiver usando um serviço como o Render ou Railway para o backend, apontar o seu **Domínio Próprio** lá no painel deles. Isso vai passar uma imagem muito profissional!

**Quer que eu te ajude a escrever a seção de "Ideia de Desenvolvimento" (o porquê você decidiu criar um RPG de tarefas) para dar um toque mais pessoal ao projeto?**
=======
# tarefas-habitos-taskos
>>>>>>> 3a7f2d1434d52f6bf37d93a7fba248c8613f54a9
