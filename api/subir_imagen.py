from appwriteClient import storage
from appwrite.input_file import InputFile
import uuid

async def subir_imagen(file,bucket):
    id = str(uuid.uuid4())
    try:
        image_content = await file.read()
        print("IMAGE CONTENT: ",image_content)
        print("CONTENT_TYPE: ",file.content_type)
        data = storage.create_file(bucket,id,InputFile.from_bytes(image_content,filename=file.filename,mime_type=file.content_type))
        return f"https://cloud.appwrite.io/v1/storage/buckets/{bucket}/files/{data['$id']}/preview?project=med-cmc&mode=admin"
    except Exception as e:
        return {"error": str(e)}