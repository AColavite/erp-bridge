# app/services/tray_product_service.py

from app.tray.client import TrayAPIClient


class TrayProductService:
    def __init__(self):
        self.client = TrayAPIClient()

    def list_products(self):
        """Lista produtos da Tray"""
        response = self.client.request("GET", "products")
        return response.get("Products", [])

    def create_product(self, product_data: dict):
        """Cria um novo produto na Tray."""

        payload = {
            "Product": product_data
        }
        response = self.client.request("POST", "products", json=payload)
        return response.get("Product", {})
