-- a script that triger when email changed
-- and change vaild_email field 

DROP TRIGGER IF EXISTS set_valid_email;

DELIMITER $$

CREATE TRIGGER set_valid_email
BEFORE UPDATE ON users FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN 
		SET NEW.valid_email = !OLD.valid_email;
	END IF;
END;
$$
