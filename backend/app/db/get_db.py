import os, sys
from dotenv import load_dotenv
load_dotenv()

from app.db.session import SessionLocal

def get_db() -> None:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
