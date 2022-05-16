CREATE DATABASE ecommerce;

USE ecommerce;

CREATE TABLE person (
	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email VARCHAR(30) NOT NULL UNIQUE,
    psw VARCHAR(32) NOT NULL
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
    product_name VARCHAR(20) NOT NULL UNIQUE,
    price DOUBLE NOT NULL
);

CREATE TABLE product_ordered (
	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    product_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (order_id) REFERENCES my_order(id)
);

INSERT INTO person(first_name, last_name, email, psw) VALUES ("root", "root", "root@gmail.com", "root2580");