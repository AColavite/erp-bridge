from pydantic import BaseModel # type: ignore
from datetime import datetime
from typing import Optional

class SyncedProductOut(BaseModel):
    id: int
    product_code: str
    name: str
    sync_status: str
    message: Optional[str]
    synced_at: datetime

    class Config:
        orm_mode = True