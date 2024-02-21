-- script that creates the MySQL server user user_0d_1
-- user_0d_1 will have all privileges on the server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- add privileges to user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
