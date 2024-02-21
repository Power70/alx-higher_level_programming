-- script that creates the table unique_id on MySQL server
-- table is created with attributes such as id which must be unique
-- and name which is a variable character
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
