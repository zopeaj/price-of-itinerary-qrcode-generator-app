import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.db.base_class import Base
from sqlalchemy import String, Integer, Column, Sequence, ForeignKey
from sqlalchemy.orm import relationship

class Product(Base):
    id = Column(Integer, Sequence("seq_product_id"), primary_key=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    vat = Column(Integer)
    itinerarybarcode = relationship("ItineraryBarcode", back_populates="product")
    itinerarybarcode_id = Column(Integer, ForeignKey("itinerarybarcode.id"))
