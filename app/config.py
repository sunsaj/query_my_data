from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQL_ALCHEMY_DATABASE_URI=os.getenv("SQL_ALCHEMY_DATABASE_URI", "sqlite:///db.sqlite3")

