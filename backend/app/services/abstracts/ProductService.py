import os, sys
from dotenv import load_dotenv
load_dotenv()
from app.models.product import Product
from app.crud.repository.productRepository import ProductRepository
from typing import Optional, List, Dict, Any

class ProductService:
    def __init__(self, productRepository):
        self.productRepository = productRepository

    def createProduct(self, product):
        pass

    def updateProduct(self, product_id, product):
        pass

    def getProduct(self, product_id):
        pass

    def deleteProduct(self, product_id):
        pass
