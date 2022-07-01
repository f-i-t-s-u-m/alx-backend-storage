-- Write a SQL script that creates a table users following these requirements:
-- with these attributes
-- id, email, name, country

CREATE TABLE IF NOT EXISTS `users` (
	`id` INT(11) AUTO_INCREMENT,
	`email` VARCHAR(255) NOT NULL UNIQUE,
	`name` VARCHAR(255),
	`country` enum('US', 'CO', 'TN') NOT NULL,
	PRIMARY KEY(`id`)
	)
