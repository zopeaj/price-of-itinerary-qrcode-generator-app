import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.models.itineraryBarcode import ItineraryBarcode
from app.models.product import Product
from app.db.get_db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

class ItineraryBarcodeRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(self, itineraryBarcode):
        pass

    def getById(self, itineraryBarcode_id):
        pass

    def update(self, itineraryBarcode_id, itineraryBarcode):
        pass

    def delete(self, itineraryBarcode_id):
        pass
