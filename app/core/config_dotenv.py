import os
from dotenv import load_dotenv

_ = load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in the environment variables.")
