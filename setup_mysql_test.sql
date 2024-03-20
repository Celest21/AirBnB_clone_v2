-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db_test;

-- Create user if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev_test'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd_test';

-- Grant all privileges on hbnb_dev_db_test to hbnb_dev_test
GRANT ALL PRIVILEGES ON hbnb_dev_db_test.* TO 'hbnb_dev_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev_test
GRANT SELECT ON performance_schema.* TO 'hbnb_dev_test'@'localhost';
