import os
from dotenv import load_dotenv

_ = load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]
