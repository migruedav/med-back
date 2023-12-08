from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from slugify import slugify

from api.heroslider import heroslider
from api.destacados import destacados
from api.biblioteca import biblioteca
from api.casosclinicos import casosclinicos
from api.ads import ads
from api.videocursos import videocursos
from api.videocursosslider import videocursosslider
from api.categoria import categoria
from api.especialidad import especialidad
from api.agregarvideocurso import agregarvideocurso
from api.borrarvideocurso import borrarvideocurso
from api.admins import admins
from api.crearpost import crearpost
from api.deploy import deploy


class Post(BaseModel):
    titulo: str
    autor: str
    categoria: str
    especialidad_principal: str
    otras_especialidades: List[str]
    es_destacado: bool
    contenido: str
    imagen: str
    hero_slider: bool
    visible: bool


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return "Este es el api de med-cmc"


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


@app.post('/agregar-video-curso')
async def agregarVideoCurso(titulo: str = Query(""), video: str = Query(""), imagen: str = Query(""), slider: bool = Query(False)):
    return agregarvideocurso(titulo, video, imagen, slider)


@app.delete('/borrar-video-curso')
async def borrarVideoCurso(id: int = Query(0)):
    return borrarvideocurso(id)


@app.get('/admins')
async def getAdmins():
    return admins()


@app.get('/especialidad')
async def getEspecialidad(esp: str = Query("")):
    return especialidad(esp)


@app.post('/crear-post')
async def crearPost(post: Post):
    return crearpost({"titulo": post.titulo, "autor": post.autor, "categoria": post.categoria, "especialidad_principal": post.especialidad_principal, "otras_especialidades": post.otras_especialidades, "es_destacado": post.es_destacado, "contenido": post.contenido, "imagen": post.imagen, "hero_slider": post.hero_slider, "visible": post.visible, "slug": slugify(post.titulo)})

@app.get('/deploy')
async def getDeploy():
    return deploy()