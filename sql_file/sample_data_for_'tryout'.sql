
INSERT INTO `tryout`.`customers` (`cust_id`, `first_name`, `phone`, `email`) 
VALUES 
('1', 'ram', NULL, NULL, '98765', 'ram@gmail.com'),
('2', 'levi', NULL, NULL, '1234', 'golu@gmail.com'),
('3', 'hich', NULL, NULL, '1928', 'hich@gmail.com'),
('4', 'eren', NULL, NULL, '5464', 'eren@gmail.com'),
('5', 'acker', NULL, NULL, '4343', 'acker@gmail.com');

INSERT INTO `tryout`.`employees` (`emp_id`, `first_name`, `last_name`, `birth_date`, `phone`, `email`) 
VALUES 
('1', 'manish', 'maurya', '1994-09-11', '12345', 'manish@gmail.com'),
('2', 'divya', 'maurya', '1997-07-31', '123456', 'divya@gmail.com');

INSERT INTO `tryout`.`orders` (`order_id`, `order_date`, `cust_id_id`, `emp_id_id`) 
VALUES 
('1', '2022-04-01', '1', '1'),
('2', '2022-03-20', '1', '2'),
('3', '2022-03-11', '2', '1'),
('4', '2022-03-02', '3', '2');

INSERT INTO `tryout`.`products` (`prod_id`, `name`, `units_remain`, `unit_price`) 
VALUES 
('1', 'cropped_jeans', '10', '700'),
('2', 'katana', '20', '1000'),
('3', 'odm', '7', '4000'),
('4', 'helmet', '10', '500');

INSERT INTO `tryout`.`orders_products` (`id`, `units`, `order_id_id`, `prod_id_id`) 
VALUES 
('1', '8', '3', '2'),
('2', '4', '1', '1'),
('3', '1', '2', '2'),
('4', '5', '4', '4');










