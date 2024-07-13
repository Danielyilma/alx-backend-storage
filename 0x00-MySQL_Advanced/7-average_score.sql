--

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INTEGER)
BEGIN
    DECLARE Avg_score FLOAT;
    SELECT AVG(score) INTO Avg_score
    FROM corrections WHERE user_id = p_user_id;

    UPDATE users
    SET average_score = Avg_score
    WHERE id = p_user_id;
END //
DELIMITER ;
