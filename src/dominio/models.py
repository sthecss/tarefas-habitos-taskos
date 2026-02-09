from dataclasses import dataclass
from datetime import datetime

@dataclass
class Tarefa:
    id: int
    titulo: str
    descricao: str
    data_limite: str  # formato YYYY-MM-DD
    status: str = 'pendente'  # 'pendente', 'progresso' ou 'concluida'
    xp: int = 50
    concluida: bool = False

    def esta_atrasada(self) -> bool:
        """verifica se a tarefa está pendente e a data já passou."""
        if self.status == 'concluida':
            return False
        hoje = datetime.now().strftime("%Y-%m-%d")
        return self.data_limite < hoy

@dataclass
class Habito:
    id: int
    nome: str
    frequencia: str  # Ex: "Diario", "Semanal", "Mensal"
    contador_execucoes: int = 0
    xp: int = 10

    def registrar_execucao(self):
        self.contador_execucoes += 1