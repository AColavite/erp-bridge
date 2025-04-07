from fastapi import APIRouter, HTTPException # type: ignore
from app.services.tray_product_service import TrayProductService

router = APIRouter()
service = TrayProductService()

@router.get("/tray/products")
def list_tray_products():
    """Lista produtos diretamente da Tray"""
    try:
        return service.list_products()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tray/products")
def create_tray_product(product_data: dict):
    """Cria um novo produto na Tray."""
    try:
        return service.create_product(product_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
