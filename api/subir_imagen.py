from appwriteClient import storage
from appwrite.input_file import InputFile
import uuid

async def subir_imagen(file):
    id = str(uuid.uuid4())
    try:
        image_content = await file.read()
        await storage.create_file('ads',id,InputFile.from_bytes(image_content,filename=file.filename,mime_type=file.content_type))
        return {"file_id": id}
    except Exception as e:
        return {"error": str(e)}