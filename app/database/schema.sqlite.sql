CREATE TABLE synced_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_code TEXT NOT NULL,
    name TEXT NOT NULL,
    sync_status TEXT NOT NULL,
    message TEXT,
    synced_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_synced_products_code ON synced_products (product_code);
CREATE INDEX idx_synced_products_status ON synced_products (sync_status);
