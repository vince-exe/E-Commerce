CREATE DATABASE ecommerce;

USE ecommerce;

CREATE TABLE person (
	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email VARCHAR(30) NOT NULL UNIQUE,
    psw VARCHAR(32) NOT NULL,
    money FLOAT
);

CREATE TABLE customer (
	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	person_id INTEGER NOT NULL UNIQUE,
    
    FOREIGN KEY (person_id) REFERENCES person(id)
);

CREATE TABLE my_order (
	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    customer_id INTEGER NOT NULL,
    
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE product (
	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(25) NOT NULL UNIQUE,
    price FLOAT NOT NULL,
    qnt INT NOT NULL
);

CREATE TABLE product_ordered (
	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    product_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    date_ DATE,

    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (order_id) REFERENCES my_order(id)
);

CREATE TABLE administrator (
	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	person_id INTEGER UNIQUE NOT NULL,

    FOREIGN KEY (person_id) REFERENCES person(id)
);

-- first insert the person and after reference the person to the administrator
INSERT INTO person(first_name, last_name, email, psw, money) VALUES ("root", "root", "root@gmail.com", "root2580", 100);
INSERT INTO administrator(person_id) VALUES (1);