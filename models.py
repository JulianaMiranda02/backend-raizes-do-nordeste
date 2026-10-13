
from dataclasses import dataclass

# Modelo de um pedido
@dataclass #permite definir uma estrutura simples para guardar os dados de cada pedido.
class Pedido:
    pedido_id: int
    cliente: str
    produto_id: int
    quantidade: int
    total: float
    status: str = "Pendente"