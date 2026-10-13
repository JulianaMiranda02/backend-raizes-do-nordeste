from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles # Importa StaticFiles, responsável por disponibilizar ficheiros estáticos
from schemas import ProdutoSchema
from mockdata import produtos


app = FastAPI()

# Configura a aplicação para disponibilizar ficheiros estáticos
app.mount(
    "/assets",
    StaticFiles(directory="assets"), # Indica a pasta onde os ficheiros estão guardados
    name="assets"  # Define um nome para identificar esta rota na aplicação
)

#verificar api funcionando
@app.get("/")
def inicio():
    return {
        "mensagem": "API do Raízes do Nordeste funcionando!"
    }

@app.get("/produtos", response_model=list[ProdutoSchema])
def listar_produtos():
    return produtos

# uvicorn main:app --reload
