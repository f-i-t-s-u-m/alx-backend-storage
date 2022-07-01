-- Write a SQL script that creates a table users following these requirements:
-- whith these attributes
-- id, email, name
-- make sure its bug free

CREATE TABLE IF NOT EXISTS `users` (
	`id` int(11) AUTO_INCREMENT,
	`email` varchar(255) NOT NULL UNIQUE,
	`name` varchar(255),
	PRIMARY KEY (`id`)
) 
