import base64
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()


def deploy():
    usuario = "migruedav"
    token = os.getenv("GIT_TOKEN")
    repo_propietario = "migruedav"
    repo_nombre = "medfront"
    ruta_archivo = "example.txt"
    branch = "main" 

    # URL del archivo en GitHub
    url = f"https://api.github.com/repos/{repo_propietario}/{repo_nombre}/contents/{ruta_archivo}?ref={branch}"

    nuevo_contenido = "Hola, mundo!\nEsta es una nueva línea."
    nuevo_contenido_codificado = base64.b64encode(nuevo_contenido.encode()).decode()


    response = requests.get(url, auth=HTTPBasicAuth(usuario, token))
    data = response.json()

    if 'sha' in data:
        sha = data['sha']
        payload = {
            "message": "Actualización de archivo desde Python",
            "content": nuevo_contenido_codificado,
            "sha": sha
        }

        response = requests.put(url, auth=HTTPBasicAuth(usuario, token), json=payload)
        if response.status_code == 200:
            return "Archivo actualizado exitosamente."
        else:
            return f"Error al actualizar el archivo. Código de estado: {response.status_code}"
    else:
        return "Error al obtener el archivo."