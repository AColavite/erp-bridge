# app/main.py
from fastapi import FastAPI # type: ignore
from app.api.v1 import product as product_router

app = FastAPI(title="ERP Bridge")

# Registrando o router da v1
app.include_router(product_router.router)

from fastapi import FastAPI # type: ignore
from app.api import router as api_router

app = FastAPI(title="ERP Integration API")
app.include_router(api_router, prefix="/api")

from app.database.session import Base, engine
from app.database import models

# Criação automática de tabelas
Base.metadata.create_all(bind=engine)
