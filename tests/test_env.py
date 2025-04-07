import pytest # type: ignore

@pytest.fixture(scope="module")
def sample_product():
    return {
        "sku": "SKU123",
        "name": "Produto Fixture",
        "price": 99.99,
        "stock": 15
    }
