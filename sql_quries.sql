-- 1. manufacturers
CREATE TABLE manufacturers (
  manufacturer_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  country VARCHAR(50),
  founded_year INT
);


-- 2. models
CREATE TABLE models (
  model_id SERIAL PRIMARY KEY,
  manufacturer_id INT NOT NULL REFERENCES manufacturers(manufacturer_id),
  model_name VARCHAR(100) NOT NULL,
  launch_year INT,
  fuel_type VARCHAR(50)
);

-- 3. sales
CREATE TABLE sales (
  sale_id SERIAL PRIMARY KEY,
  model_id INT NOT NULL REFERENCES models(model_id),
  sale_date DATE,
  units_sold INT,
  sale_price NUMERIC(10,2),
  region VARCHAR(50)
);
