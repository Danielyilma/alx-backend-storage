--

DELIMITER //
CREATE  PROCEDURE AddBonus(user_id INTEGER, project_name varchar(255), score INTEGER)
BEGIN
    DECLARE project_id INTEGER;
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    if project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //
DELIMITER ;