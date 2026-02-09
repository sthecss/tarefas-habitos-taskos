from src.dominio.models import Tarefa, Habito

def obter_tarefas_atrasadas(tarefas: list[Tarefa]) -> list[Tarefa]:
    return [t for t in tarefas if t.esta_atrasada()]

def obter_tarefas_pendentes(tarefas: list[Tarefa]) -> list[Tarefa]:
    return [t for t in tarefas if not t.concluida]

def obter_ranking_habitos(habitos: list[Habito]) -> list[Habito]:
    return sorted(habitos, key=lambda h: h.contador_execucoes, reverse=True)