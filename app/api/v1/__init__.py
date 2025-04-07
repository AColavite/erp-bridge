from .product import router as product_router

from fastapi import APIRouter # type: ignore
from app.api.v1 import product, tray_product

router = APIRouter()
router.include_router(product.router, prefix="/products", tags=["Products"])
router.include_router(tray_product.router, tags=["Tray Products"])

from fastapi import APIRouter # type: ignore
from .product import router as product_router
from .tray_product import router as tray_router
from .sync import router as sync_router 

router = APIRouter()
router.include_router(product_router)
router.include_router(tray_router)
router.include_router(sync_router)
