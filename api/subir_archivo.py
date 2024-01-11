from appwriteClient import storage
from appwrite.input_file import InputFile
import uuid

async def subir_archivo(file,bucket):
    id = str(uuid.uuid4())
    try:
        image_content = await file.read()
        data = storage.create_file(bucket,id,InputFile.from_bytes(image_content,filename=file.filename,mime_type=file.content_type))
        return f"https://cloud.appwrite.io/v1/storage/buckets/{bucket}/files/{data['$id']}/view?project=med-cmc&mode=admin"
    except Exception as e:
        return {"error": str(e)}