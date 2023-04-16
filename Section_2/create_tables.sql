CREATE TABLE members (
    member_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    above_18 BOOLEAN NOT NULL
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(50) NOT NULL,
    manufacturer_name VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    weight DECIMAL(10,2) NOT NULL
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    member_id VARCHAR REFERENCES members(member_id) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    total_weight DECIMAL(10,2) NOT NULL
);

CREATE TABLE transaction_details (
    detail_id SERIAL PRIMARY KEY,
    transaction_id INTEGER REFERENCES transactions(transaction_id) NOT NULL,
    item_id INTEGER REFERENCES items(item_id) NOT NULL,
    quantity INTEGER NOT NULL
);

-- add index on foreign keys to improve performance of joins and lookups
CREATE INDEX member_id_idx ON transactions(member_id);
CREATE INDEX transaction_id_idx ON transaction_details(transaction_id);
