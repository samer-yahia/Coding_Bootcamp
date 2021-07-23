SELECT * FROM dojos_and_ninjas_schema.dojos;

SET SQL_SAFE_UPDATES = 0;

-- Query: Create 3 new dojos

INSERT INTO dojos (name) 
VALUES ('Chris'), 
	('Rashad');
SELECT * FROM dojos;


-- Query: Delete the 3 dojos you just created
-- DELETE 
-- sql command: DELETE
-- DELETE FROM <tablename> WHERE id = <value>;
-- DELETE FROM orders; 

DELETE FROM dojos;
SELECT * FROM dojos;


-- Query: Create 3 more dojos 

INSERT INTO dojos (name) 
VALUES ("Chris's Dojo"), 
	("Rashad's Dojo"), 
	("Iskander's Dojo");
SELECT * FROM dojos;


-- Query: Create 3 ninjas that belong to the first dojo


INSERT INTO ninjas (dojo_id, first_name, last_name, age) 
VALUES (4, "Samer", "Yahia", 27), 
	(4, "Iskander", "Rangel", 26), 
	(4, "Chris", "Engel", 21);
SELECT * FROM ninjas;


-- Query: Create 3 ninjas that belong to the second dojo

INSERT INTO ninjas (dojo_id, first_name, last_name, age) 
VALUES (5, "Shivam", "Dutta", 22), 
	(5, "Rashad", "Naime", 11), 
    (5, "Chris", "Engel", 21);
SELECT * FROM ninjas;


-- Query: Create 3 ninjas that belong to the third dojo


INSERT INTO ninjas (dojo_id, first_name, last_name, age) 
VALUES (6, "Christian", "L", 25), 
	(6, "Rayan", "Yahia", 100), 
	(6, "Samer", "Yahia", 21);
SELECT * FROM ninjas;


-- Query: Retrieve all the ninjas from the first dojo

SELECT * FROM dojo;


-- Query: Retrieve all the ninjas from the last dojo

-- Query: Retrieve the last ninja's dojo 





