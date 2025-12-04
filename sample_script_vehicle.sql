CREATE DATABASE vehicles;

-- 1️⃣ Manufacturers Table
CREATE TABLE manufacturers (
    manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    founded_year INT
);

-- 2️⃣ Vehicle Models Table
CREATE TABLE vehicle_models (
    model_id INT AUTO_INCREMENT PRIMARY KEY,
    manufacturer_id INT,
    model_name VARCHAR(100) NOT NULL,
    vehicle_type ENUM('Sedan','SUV','Hatchback','Truck','Electric','Hybrid'),
    engine_type VARCHAR(50),
    launch_year INT,
    price DECIMAL(10,2),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id)
);

-- 3️⃣ Sales Table
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    model_id INT,
    sale_year INT,
    units_sold INT,
    region VARCHAR(50),
    FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id)
);
