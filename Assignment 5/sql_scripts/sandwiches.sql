
CREATE TABLE IF NOT EXISTS sandwiches (
id int NOT NULL AUTO_INCREMENT,
sandwich_size varchar(50) NOT NULL,
price decimal(5, 2) NOT NULL,
PRIMARY KEY (id)
);

SELECT * FROM sandwiches;
