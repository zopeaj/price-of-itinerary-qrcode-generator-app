import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter
from app.api_v1.controller.itineraryBarcodeGeneratorController import itineraryBarcodeRoutes

api_router = APIRouter()
api_router.include_router(itineraryBarcodeRoutes, prefix="/api/v1/itinerary-barcode-generator", tags=["itinerary-barcode-generator"])

