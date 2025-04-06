# app/services/product_service.py

from typing import List
from app.erp.client import erp_client
from app.models.product import Product, ProductCreate


def list_products() -> List[Product]:
    erp_response = erp_client.get_products()

    if not erp_response:
        return []

    products = []
    for item in erp_response:
        try:
            product = Product(
                id=0,  # If ERP has no ID, use HASH or 0
                sku=item.Codigo,
                name=item.Descricao,
                description=None,
                price=item.PrecoVenda or 0.0,
                stock=item.Estoque or 0
            )
            products.append(product)
        except Exception as e:
            print(f"Erro ao converter produto: {e}")
            continue

    return products


def create_product(product_data: ProductCreate):
    payload = {
        "Codigo": product_data.sku,
        "Descricao": product_data.name,
        "Estoque": product_data.stock,
        "PrecoVenda": product_data.price,
    }

    return erp_client.create_product(payload)
