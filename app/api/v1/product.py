from fastapi import APIRouter, HTTPException, status # type: ignore
from typing import List

from app.models.product import Product, ProductCreate
from app.services.product_service import list_products, create_product

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=List[Product])
def get_products():
    try:
        return list_products()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar produtos: {str(e)}")


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_product(product: ProductCreate):
    try:
        result = create_product(product)
        if result.get("success"):
            return {"message": "Produto criado com sucesso no ERP"}
        else:
            raise HTTPException(status_code=400, detail="Falha ao criar produto no ERP")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar produto: {str(e)}")
