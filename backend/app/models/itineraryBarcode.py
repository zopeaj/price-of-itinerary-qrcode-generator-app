import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.db.base import Base
from sqlalchemy import String, Column, Integer, Sequence, ForeignKey
from sqlalchemy.orm import relationship

class ItineraryBarcode(Base):
    id = Column(Integer, primary_key=True)
    codedata = Column(String)
    product = relationship("Product", back_populates="itinerarybarcode")
    product_id = Column(Integer, ForeignKey("product.id"))
