from pydantic import BaseModel, Field

# Representa os dados completos de um produto
class ProdutoSchema(BaseModel):
    id: int
    nome: str
    preco: float = Field(gt=0)
    categoria: str
    link_imagem: str



