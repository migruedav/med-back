async def subir_imagen(file):

    try:
        image_content = await file.read()

        with open(f"./{file.filename}", "wb") as f:
            f.write(image_content)

        return {"message": "Imagen subida y guardada exitosamente en el servidor"}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}
