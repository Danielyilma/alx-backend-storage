--

CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 AND (last_meeting IS NULL or (DATEDIFF(CURDATE(), last_meeting) > 30));