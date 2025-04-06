from pydantic import BaseModel, Field # type: ignore
from typing import Optional

class Product(BaseModel):
    id: int
    sku: str
    name: str
    description: Optional[str]
    price: float
    stock: int

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    sku: str = Field(..., example="PROD001")
    name: str = Field(..., example="Produto Exemplo")
    description: Optional[str] = Field(None, example="Descrição do produto")
    price: float = Field(..., example=199.90)
    stock: int = Field(..., example=50)

class ProductInERP(BaseModel):
    Codigo: str
    Descricao: str
    Estoque: Optional[int]
    PrecoVenda: Optional[float]