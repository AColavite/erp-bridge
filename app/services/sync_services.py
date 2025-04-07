from app.services.product_service import ERPProductService
from app.services.tray_product_service import TrayProductService
from app.models.product import Product
from app.database.models import SyncedProduct
from app.database.session import SessionLocal
from typing import List, Dict


class SyncService:
    def __init__(self):
        self.erp = ERPProductService()
        self.tray = TrayProductService()
        self.db = SessionLocal()

    def sync_erp_to_tray(self) -> Dict:
        erp_products: List[Product] = self.erp.list_products()
        tray_existing = self.tray.list_products()

        existing_codes = {p["product_code"] for p in tray_existing}
        sync_results = {"created": [], "skipped": [], "failed": []}

        for product in erp_products:
            code = product.product_code
            name = product.name

            """Verifica se o produto já existe na Tray"""
            if code in existing_codes:
                self._save_sync_result(code, name, "skipped", "Produto já existente na Tray")
                sync_results["skipped"].append(code)
                continue

            try:
                tray_payload = self._transform_for_tray(product)
                response = self.tray.create_product(tray_payload)

                if response.get("id") or response.get("success"):
                    self._save_sync_result(code, name, "created", "Criado com sucesso")
                    sync_results["created"].append(code)
                else:
                    msg = response.get("message") or "Erro não especificado"
                    self._save_sync_result(code, name, "failed", msg)
                    sync_results["failed"].append({code: msg})
            except Exception as e:
                self._save_sync_result(code, name, "failed", str(e))
                sync_results["failed"].append({code: str(e)})

        self.db.commit()
        self.db.close()
        return sync_results

    def _transform_for_tray(self, product: Product) -> dict:
        return {
            "product_code": product.product_code,
            "name": product.name,
            "description": product.description or "",
            "price": f"{product.price:.2f}",
            "quantity": str(product.quantity),
            "status": "1"  
        }

    def _save_sync_result(self, code: str, name: str, status: str, message: str):
        record = SyncedProduct(
            product_code=code,
            name=name,
            sync_status=status,
            message=message
        )
        self.db.add(record)

class SyncService:
    def __init__(self):
        self.erp = ERPProductService()
        self.tray = TrayProductService()
        self.db = SessionLocal()
        self.model = SyncedProduct  

