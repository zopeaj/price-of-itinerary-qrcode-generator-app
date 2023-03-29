import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.crud.repository.itineraryBarcodeRepository import ItenraryBarcodeRepository
from app.models.itineraryBarcode import ItineraryBarcode

class ItineraryBarcodeService:
    def __init__(self, itineraryBarcodeRepository):
        self.itineraryBarcodeRepository = itineraryBarcodeRepository

    def createItineraryBarcodeData(self, itineraryBarcode):
        return self.itineraryBarcodeRepository.save(itineraryBarcode)

    def updateItineraryBarcodeData(self, itineraryBarcode_id, itineraryBarcodeUpdate):
        return self.itineraryBarcodeRepository.update(itineraryBarcode_id, itineraryBarcodeUpdate)

    def deleteItineraryBarcodeData(self, itineraryBarcode_id):
        return self.itineraryBarcodeRepository.delete(itineraryBarcode_id)

    def getItineraryBarcodeData(self, itineraryBarcode_id):
        return self.itineraryBarcodeRepository.getbyId(itineraryBarcode_id)
