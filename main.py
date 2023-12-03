from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.prueba import prueba
from api.heroslider import heroslider
from api.destacados import destacados
from api.biblioteca import biblioteca
from api.casosclinicos import casosclinicos



app = FastAPI()

origins = ["https://www.med-cmc.com","http://localhost:4321"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {'message':'TQREC'}

@app.get('/hero-slider')
async def getHeroSlider():
    return heroslider()

@app.get('/destacados')
async def getDestacados():
    return destacados()

@app.get('/biblioteca')
async def getBiblioteca():
    return biblioteca()

@app.get('/casos-clinicos')
async def getCasosClinicos():
    return casosclinicos()


