from time import time
from fastapi import FastAPI, __version__
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return {'message':'TQREC'}

@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}