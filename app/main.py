# app/main.py
from fastapi import FastAPI # type: ignore
from app.api.v1 import product as product_router

app = FastAPI(title="ERP Bridge")

# Registrando o router da v1
app.include_router(product_router.router)
