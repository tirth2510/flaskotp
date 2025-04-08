# firebase_init.py
import os
from firebase_admin import credentials, firestore, initialize_app
from dotenv import load_dotenv

load_dotenv()

cred_path = os.getenv("GOOGLE_CREDENTIALS")
if not cred_path:
    raise Exception("GOOGLE_CREDENTIALS environment variable not set")

cred = credentials.Certificate(cred_path)
initialize_app(cred)
db = firestore.client()
