from fastapi import APIRouter, HTTPException      # type: ignore
from app.services.sync_service import SyncService # type: ignore

router = APIRouter()
sync_service = SyncService()

@router.post("/sync/products", tags=["Sync"])
def sync_products_erp_to_tray():
    try:
        result = sync_service.sync_erp_to_tray()
        return {"message": "Sync completed", "synced_count": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# app/api/v1/sync.py

from fastapi import APIRouter, HTTPException, Depends, Query # type: ignore
from sqlalchemy.orm import Session                          # type: ignore
from typing import List

from app.services.sync_service import SyncService           # type: ignore
from app.database.schemas import SyncedProductOut
from app.database.session import SessionLocal

router = APIRouter()
sync_service = SyncService()

"""Dependency para injetar o DB"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sync/products", tags=["Sync"])
def sync_products_erp_to_tray():
    try:
        result = sync_service.sync_erp_to_tray()
        return {"message": "Sync completed", **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sync/history", response_model=List[SyncedProductOut], tags=["Sync"])
def get_sync_history(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, le=100),
    db: Session = Depends(get_db)
):
    try:
        records = db.query(sync_service.model).order_by(sync_service.model.synced_at.desc()).offset(skip).limit(limit).all()
        return records
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
