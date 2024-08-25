CREATE DATABASE challenge;
USE challenge;

CREATE TABLE customers(
	coustomer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    address VARCHAR(50)
);
INSERT INTO customers (name, address) VALUES ('chang su', '율하동');
ALTER TABLE customers ADD city VARCHAR(50); -- customers 테이블에 city Column 추가
INSERT INTO customers (name, address, city) VALUES ('Jane Smith', '456 Elm St', 'New York');

CREATE TABLE products(
	product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    price INT
);
INSERT INTO products (name, price) VALUES ('Toy Car', 19.99);
ALTER TABLE products ADD productLine VARCHAR(100); -- products 테이블에 productLine Column 추가
INSERT INTO products (name, price, productLine) VALUES ('Vintage Train', 34.99, 'Trains');

CREATE TABLE employees(
	employee_id INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(30),
    lastName VARCHAR(30)
);
INSERT INTO employees (firstName, lastName) VALUES ('Alice', 'Johnson');

CREATE TABLE orders(
	order_id INT PRIMARY KEY AUTO_INCREMENT,
 order_Date DATE,
 customerID INT,
 FOREIGN KEY (order_id) REFERENCES customers(coustomer_id)
);
INSERT INTO orders (order_Date, customerID) VALUES ('2023-01-01', 1);

CREATE TABLE orderdetails(
	order_datatil_id INT PRIMARY KEY AUTO_INCREMENT,
    orderID INT,
    productID INT,
	quantityOrdered INT,
    priceEach INT
);
INSERT INTO orderdetails (orderID, productID, quantityOrdered, priceEach) VALUES (1, 1, 2, 20.00);

CREATE TABLE payments(
	payment INT PRIMARY KEY AUTO_INCREMENT,
    customerID INT,
    amount INT,
    paymentDate DATE
);
INSERT INTO payments (customerID, amount, paymentDate) VALUES (1, 200.00, '2023-01-01');

CREATE TABLE productlines(
	productline_id INT PRIMARY KEY AUTO_INCREMENT,
    productLine VARCHAR(100),
    textDescription VARCHAR(200)
);
INSERT INTO productlines (productLine, textDescription) VALUES ('Classic Cars', 'Various classic cars models');

