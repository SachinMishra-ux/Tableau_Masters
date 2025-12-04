CREATE TABLE orders_raw (
    order_id VARCHAR,
    customer_id VARCHAR,
    product_name VARCHAR,
    order_date VARCHAR,
    order_amount VARCHAR,
    payment_status VARCHAR,
    shipping_city VARCHAR
);


INSERT INTO orders_raw VALUES
('O1001','C001','iphone 14 ','2024-02-01','$1200','Success','Bangalore'),
('O1002','C002','Samsung S22','01/02/24','950 USD','Failed','Bengaluru'),
('O1003','C003','Macbook  pro','2024/02/03','1500','Success','Bangalore '),
('O1004','C004','IPHONE14','2024.02.05','Na','Success','Bengaluru'),
('O1005','C005','Iphone-14','2024-02-10','1200$','Pending','Banglore'),
('O1006','','Samsung   s22','2024-02-11','950','Success','Bangalore'),
('O1007','C007','-','2024-02-13','700','Failed','Unknown'),
('O1008','C008','Airpods   Pro','14-02-2024','250 USD','Success','Hyderabad'),
('O1009','C009','Samsung S22','2024/02/15','950','Success','NA'),
('O1010','C001','iphone 14 ','2024-02-01','$1200','Success','Bangalore');  -- duplicate

