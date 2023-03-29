import os, sys
from dotenv import load_dotenv
load_dotenv()
from app.models.product import Product
from fastapi import Depends
from app.db.get_db import get_db
from sqlalchemy.orm import Session

class ProductRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(self, product):
        pass

    def getById(self, product_id):
        pass

    def update(self, product_id, product):
        pass

    def delete(self, product_id):
        pass

