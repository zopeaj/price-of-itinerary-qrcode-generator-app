import sys, os

path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter, FastAPI
from app.api_v1.routes import api_router

app = FastAPI(title="", openapi_url="")
app.include_router(api_router, prefix="", tags=[""])
