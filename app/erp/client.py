from zeep import Client # type: ignore
from zeep.transports import Transport # type: ignore
from requests import Session # type: ignore
from requests.auth import HTTPBasicAuth # type: ignore
from app.core.config import settings

class ERPClient:
    def __init__(self):
        session = session()
        session.auth = HTTPBasicAuth(settings.ERP_USERNAME, settings.ERP_PASSWORD)

        self.client = Client(
            wsdl=settings.ERP_WSDL_URL,
            transport = Transport(session=session)
        )

    def get_products(self):
        try:
            response = self.client.service.ListarProdutos()
            return response
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")
            return None
        
    def create_product(self, data):
        try:
            response = self.client.service.CadastrarProduto(data)
            return response
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}")
            return None
        
erp_client = ERPClient()
            
        