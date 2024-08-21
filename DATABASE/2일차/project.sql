-- < 과제 1 >
-- mysql 로그인
mysql -u root -p

-- 사용자 생성
CREATE USER 'fishbread_user'@'localhost' IDENTIFIED BY 'fish';

-- 사용자 권한부여 및 적용
GRANT ALL PRIVILEGES ON . TO 'fishbread_user'@'localhost';
FLUSH PRIVILEGES;

-- 권환 확인
SHOW GRANTS FOR 'fishbread_user'@'localhost';

-- < 과제 2 >
-- 데이터베이스 생성
CREATE DATABASE fishbread_db;

-- 데이터베이스 사용
USE fishbread_db;

-- user table 생성
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) UNIQUE,
    is_business BOOLEAN DEFAULT FALSE
);

-- order table 생성
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- inventory table 생성
CREATE TABLE inventory (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL
);

-- sales table 생성
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    item_id INT,
    quantity_sold INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id) REFERENCES inventory(item_id)
);

-- dailt]y_sales table 생성
CREATE TABLE daily_sales (
    date DATE PRIMARY KEY,
    total_sales DECIMAL(10, 2) NOT NULL
);