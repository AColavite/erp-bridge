from pydantic import BaseSettings # type: ignore

class Settings(BaseSettings):
    ERP_WSDL_URL: str
    ERP_USERNAME: str
    ERP_PASSWORD: str

    class Config:
        env_file = ".env"

settings = Settings()