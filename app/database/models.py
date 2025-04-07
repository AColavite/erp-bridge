from sqlalchemy import Column, Integer, String, DateTime # type: ignore
from datetime import datetime
from app.database.session import Base

class SyncedProduct(Base):
    __tablename__ = "synced_products"

    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String, index=True)
    name = Column(String)
    sync_status = Column(String)  # "created", "skipped", "failed"
    message = Column(String, nullable=True)
    synced_at = Column(DateTime, default=datetime.utcnow)
