import pyqrcode
from uuid import uuid4
import random

class ItineraryBarcodeGeneratorService:
    def __init__(self):
        self.filename = f'{uuid4().hex}'
        self.scalenumber = 8

    def generateQRCode(self, datatoencode):
        return self.generateData(datatoencode)

    def lookUpQrCode(self, filename):
        return self.lookUpData(filename)

    def generateData(self, datatoencode):
        qrcode = pyqrcode.create(datatoencode)
        filename = f'{self.filename}.png'
        qrcode.png(filename, scale=self.scalenumber)
        return filename

    def lookUpData(self, filename):
        with open(filename, 'rb') as f:
            content = f.read()
            return content

