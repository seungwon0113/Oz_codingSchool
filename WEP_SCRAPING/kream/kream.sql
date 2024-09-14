CREATE DATABASE kream;

USE kream;

CREATE TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    product_brand VARCHAR(255) NOT NULL,
    product_price DECIMAL(10, 2) NOT NULL
);    
