from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.prueba import prueba
from api.heroslider import heroslider



app = FastAPI()

origins = ["http://localhost:4321","https://www.med-cmc.com/"]

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
