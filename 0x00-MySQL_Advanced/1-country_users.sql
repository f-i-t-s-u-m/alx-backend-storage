-- Write a SQL script that creates a table users following these requirements:
-- with these attributes
-- id, email, name, country

CREATE TABLE IF NOT EXISTS `users` (
	`id` int(11) AUTO_INCREMENT,
	`email` varchar(255) not null unique,
	`name` varchar(255),
	`country` enum('US', 'CO', 'TN') default('US') not null,
	PRIMARY KEY(`id`)
	)
