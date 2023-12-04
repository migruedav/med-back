from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from api.heroslider import heroslider
from api.destacados import destacados
from api.biblioteca import biblioteca
from api.casosclinicos import casosclinicos
from api.ads import ads
from api.videocursos import videocursos
from api.videocursosslider import videocursosslider
from api.categoria import categoria



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

@app.get('/ads')
async def getAds(position: str = Query("top")):
    return ads(position)

@app.get('/video-cursos')
async def getVideoCursos():
    return videocursos()

@app.get('/video-cursos-slider')
async def getVideoCursos():
    return videocursosslider()

@app.get('/categoria')
async def getCategoria(cat: str = Query("")):
    return categoria(cat)

