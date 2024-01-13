from appwrite.client import Client
from appwrite.services.storage import Storage
from appwrite.services.databases import Databases
from appwrite.services.users import Users
from appwrite.query import Query
import os
from dotenv import load_dotenv
load_dotenv()

client = Client()
key = os.getenv("APPWRITE_KEY")

(client
  .set_endpoint('https://cloud.appwrite.io/v1')
  .set_project('med-cmc')
  .set_key(key) # Your secret API key
)

storage = Storage(client)
db = Databases(client)
users = Users(client)
q = Query()
