from dotenv import load_dotenv
import os
load_dotenv()



def prueba ():
    return {"prueba":os.getenv("PRUEBA")}