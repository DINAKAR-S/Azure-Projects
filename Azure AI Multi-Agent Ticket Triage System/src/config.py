import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
MODEL_DEPLOYMENT = os.getenv("MODEL_DEPLOYMENT")

if not PROJECT_ENDPOINT or not MODEL_DEPLOYMENT:
    raise ValueError("Missing required environment variables")