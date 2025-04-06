erp-bridge/
├── app/
│   ├── api/                    # Rotas da API REST
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── product.py      # Endpoints relacionados a produtos
│   │
│   ├── core/                   # Configurações e constantes
│   │   ├── __init__.py
│   │   └── config.py           # WSDL, env vars, logs
│   │
│   ├── erp/                    # Cliente e lógica de integração com o ERP (via SOAP)
│   │   ├── __init__.py
│   │   └── client.py           # Lógica de chamada SOAP
│   │
│   ├── models/                 # Modelos Pydantic usados pela API
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   ├── services/               # Regras de negócio (caso queira abstrair o client SOAP aqui)
│   │   ├── __init__.py
│   │   └── product_service.py
│   │
│   ├── main.py                 # Ponto de entrada da aplicação FastAPI
│
├── tests/                      # Testes automatizados
│   ├── __init__.py
│   └── test_product.py
│
├── requirements.txt
├── README.md
└── .env                        # Variáveis de ambiente (WSDL, autenticação, etc)
