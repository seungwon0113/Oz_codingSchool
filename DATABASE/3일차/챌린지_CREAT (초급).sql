-- CREATE DATABASE challenge;

-- USE challenge;

-- CREATE TABLE employees (
-- 	id INT PRIMARY KEY AUTO_INCREMENT,
-- 	name VARCHAR(100),
--     position VARCHAR(100),
-- 	salary DECIMAL(10,2)
-- );

-- INSERT INTO employees (name, position, salary) VALUES ('혜린', 'PM', 90000);
-- INSERT INTO employees (name, position, salary) VALUES ('은우', 'Frontent', 80000);
-- INSERT INTO employees (name, position, salary) VALUES ('가을', 'Backend', 92000);
-- INSERT INTO employees (name, position, salary) VALUES ('지수', 'Frontend', 78000);
-- INSERT INTO employees (name, position, salary) VALUES ('민혁', 'Frontend', 96000);
-- INSERT INTO employees (name, position, salary) VALUES ('하온', 'Backend', 130000);

-- SELECT name salary FROM employees  WHERE position = 'Frontend' AND salary <= 90000;

-- SET SQL_SAFE_UPDATES = 0; : Safe Mode 끄기 >> Error Code 1175
-- UPDATE employees SET salary = salary * 1.10 WHERE position = 'PM'; : PM 10% 연봉인상
-- SELECT * FROM employees WHERE position = 'Quality Assurance';

-- UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend'; : Backend 5% 연봉 인상

-- DELETE FROM employees WHERE name = '민혁'; : 민혁 데이터 삭제

SELECT position, AVG(salary) AS average_salary FROM employees GROUP BY position;

SELECT * FROM employees;