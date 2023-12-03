from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {'message':'TQREC'}

@app.get('/ada')
async def hello():
    return {'message':'Hello TQREC2'}
