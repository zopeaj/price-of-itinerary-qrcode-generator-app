from pydantic import BaseModel
from typing import List, Optional, Any, Dict

class ProductInDB(BaseModel):
    pass

class ProductCreate(ProductInDB):
    pass

class ProductUpdate(ProductInDB):
    pass

class ProductDelete(ProductInDB):
    pass

