from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles # Importa StaticFiles, responsável por disponibilizar ficheiros estáticos
from fastapi.middleware.cors import CORSMiddleware

from schemas import ProdutoSchema
from mockdata import produtos


app = FastAPI(title='Projeto API produtos com FastAPI')

# Configurações do CORS
app.add_middleware( 
   CORSMiddleware, 
    allow_origins=[
        "http://localhost:4200", # URL do seu frontend 
    ],
   allow_credentials=True, 
   allow_methods=["*"], 
   allow_headers=["*"], 
) 

   
# Configura a aplicação para disponibilizar ficheiros estáticos
app.mount(
    "/assets",
    StaticFiles(directory="assets"), # Indica a pasta onde os ficheiros estão guardados
    name="assets"  # Define um nome para identificar esta rota na aplicação
)

# Verificar se  a API  está  funcionando
@app.get("/")
def inicio():
    return {
        "mensagem": "API do Raízes do Nordeste funcionando!"
    }


# Listar produtos
@app.get("/produtos", response_model=list[ProdutoSchema])
def listar_produtos():
    return produtos


#  Executar a API
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=True
    )

# uvicorn main:app --reload
