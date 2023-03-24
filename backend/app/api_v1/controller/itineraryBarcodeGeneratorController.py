import os, sys
from dotenv import load_dotenv
load_dotenv()

from fastapi import APIRouter, Response, Request, Path
from app.services.ItineraryBarcodeGeneratorService import ItineraryBarcodeGeneratorService

itineraryBarcodeRoutes = APIRouter()

@itineraryBarcodeRoutes.post("/")
def create_barcode_for_product():
    pass

@itineraryBarcodeRoutes.get("/")
def get_barcode_for_product():
    pass

