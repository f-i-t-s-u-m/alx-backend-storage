-- sql script that creates a stored procedure AddBonus that adds
-- a new correction for a student
-- Procedure AddBonus is taking 3 inputs (in this order)
--  user_id, a users.id value (you can assume user_id is linked to an existing users)
--  project_name, a new or already exists projects - 
--   --- if no projects.name found in the table, you should create it
--  score, the score value for the correction


DELIMITER $$
CREATE PROCEDURE AddBonus
(user_id int, project_name varchar (255), score float)


BEGIN
	 INSERT INTO projects (name)
    SELECT project_name FROM DUAL

    WHERE NOT EXISTS (SELECT * FROM projects WHERE name = project_name);
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
	
END $$
