CREATE DATABASE IF NOT EXISTS app_db;
USE app_db;

CREATE TABLE datos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT
);

INSERT INTO datos (nombre, edad) VALUES
('Juan', 25),
('Maria', 30);
