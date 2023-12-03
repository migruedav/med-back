from fastapi import FastAPI
from api.prueba import prueba


app = FastAPI()

@app.get("/")
async def root():
    return {'message':'TQREC'}

@app.get('/ada')
async def hello():
    return {'message':'Hello TQREC2'}

@app.get('/prueba')
async def getprueba():
    return prueba()
