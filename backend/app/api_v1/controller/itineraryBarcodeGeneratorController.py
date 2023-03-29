import os, sys
from dotenv import load_dotenv
load_dotenv()

from fastapi import APIRouter, Response, Request, Path
from app.services.ItineraryBarcodeGeneratorService import ItineraryBarcodeGeneratorService
from app.services.abstracts.ItineraryBarcodeService import ItineraryBarcodeService
from app.services.abstracts.ProductService import ProductService
from app.schema.productSchema import ProductCreate
from app.schema.itinerarySchema import ItineraryCreate

itineraryBarcodeRoutes = APIRouter()
itineraryBarcodeGeneratorSerice = ItineraryBarcodeGeneratorService()
itineraryBarcodeService = ItineraryBarcodeService()
productService = ProductService()


@itineraryBarcodeRoutes.post("/")
def create_barcode_for_product(request: Request):
    pass



@itineraryBarcodeRoutes.get("/")
def get_barcode_for_product():
    pass

