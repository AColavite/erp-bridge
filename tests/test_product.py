# tests/test_product.py
import pytest # type: ignore
from httpx import AsyncClient # type: ignore
from fastapi import status # type: ignore

from app.main import app
from app.models.product import ProductCreate


@pytest.mark.asyncio
async def test_get_products():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/products/")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_post_product(monkeypatch):

    def mock_create_product(product_data):
        return {"success": True}

    from app.services import product_service
    monkeypatch.setattr(product_service, "create_product", mock_create_product)

    payload = {
        "sku": "TEST001",
        "name": "Produto Teste",
        "description": "Descrição de teste",
        "price": 123.45,
        "stock": 10
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/products/", json=payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["message"] == "Produto criado com sucesso no ERP"
