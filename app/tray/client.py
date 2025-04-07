# app/tray/client.py

import requests # type: ignore
import os
from typing import Optional
from dotenv import load_dotenv # type: ignore

load_dotenv()

TRAY_BASE_URL = f"https://{os.getenv('TRAY_STORE')}.api.tray.com.br"
CLIENT_ID = os.getenv("TRAY_CLIENT_ID")
CLIENT_SECRET = os.getenv("TRAY_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("TRAY_REFRESH_TOKEN")


class TrayAPIClient:
    def __init__(self):
        self.access_token: Optional[str] = None

    def authenticate(self):
        """Obtém novo access_token usando o refresh_token"""
        url = f"{TRAY_BASE_URL}/auth/token"
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": REFRESH_TOKEN,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }

        response = requests.post(url, data=payload)
        response.raise_for_status()

        data = response.json()
        self.access_token = data.get("access_token")

    def _get_headers(self):
        if not self.access_token:
            self.authenticate()

        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def request(self, method: str, endpoint: str, params=None, data=None, json=None):
        """Faz uma requisição genérica à API da Tray"""
        url = f"{TRAY_BASE_URL}/web_api/{endpoint}"
        headers = self._get_headers()

        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            data=data,
            json=json
        )

        if response.status_code == 401:
            self.authenticate()
            headers = self._get_headers()
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json
            )

        response.raise_for_status()
        return response.json()
