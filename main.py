from fastapi import FastAPI, Query,File, UploadFile, Body
from typing import Dict, Any,List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

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
from api.registro import registro
from api.crearusuario import crearusuario
from api.medicosexamenes import medicosexamenes
from api.all_posts import all_posts
from api.especialidad_related import especialidad_related
from api.examenes import examenes
from api.subir_imagen import subir_imagen
from api.subir_archivo import subir_archivo
from api.editar_post import editar_post
from api.borrar_post import borrar_post
from api.borrar_ad import borrar_ad
from api.agregar_ad import agregar_ad
from api.all_ads import all_ads
from api.agregar_examen import agregar_examen
from api.agregar_pyr import agregar_pyr


class Registro(BaseModel):
    nombre: str
    apellido: str
    email: str
    cedula: str
    especialidad: str
    pais: str
    estado: str


class CrearUsuario(BaseModel):
    email: str
    password: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
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
async def crearPost(post: dict):
    return crearpost(post)


@app.get('/deploy')
async def getDeploy():
    return deploy()


@app.post('/registro')
async def sendRegistro(reg: Registro):
    return registro({"nombre": reg.nombre, "apellido": reg.apellido, "email": reg.email, "cedula": reg.cedula, "especialidad": reg.especialidad, "pais": reg.pais, "estado": reg.estado})


@app.post('/crear-usuario')
async def setCrearUsuario(usr: CrearUsuario):
    return crearusuario({"email": usr.email, "password": usr.password})


@app.get('/medicos-examenes')
async def getMedicosExamenes():
    return medicosexamenes()

@app.get('/all-posts')
async def getAllPosts(offset: int = Query(0)):
    return all_posts(offset)

@app.get('/especialidad-related')
async def getEspecialidadRelated(esp: str = Query("")):
    return especialidad_related(esp)

@app.get('/examenes')
async def getExamenes(offset: int = Query(0)):
    return examenes(offset)

@app.post('/subir-imagen')
async def subirImagen(file: UploadFile = File(...),bucket:str = Query("posts")):
    return await subir_imagen(file,bucket)

@app.post('/subir-archivo')
async def subirArchivo(file: UploadFile = File(...),bucket:str = Query("posts")):
    return await subir_archivo(file,bucket)

@app.post('/editar-post')
async def editarPost(post: dict,id: str = Query("")):
    return editar_post(post,id)

@app.delete('/borrar-post')
async def borrarPost(id: str):
    return borrar_post(id)

@app.delete('/borrar-ad')
async def borrarAd(id: str):
    return borrar_ad(id)

@app.post('/agregar-ad')
async def agregarAd(ad: dict):
    return agregar_ad(ad)

@app.get('/all-ads')
async def getAllAds():
    return all_ads()

@app.post('/agregar-examen')
async def agregarExamen(examen: dict):
    return agregar_examen(examen)

@app.post('/agregar-pyr')
async def agregarPyr(post: dict):
    return agregar_pyr(post)