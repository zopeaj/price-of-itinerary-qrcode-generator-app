from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(url=, echo=True)
SessionLocal = sessionmaker(autofocus=False, autocommit=False, bind=engine)
