-- 

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN p_user_id INTEGER)
BEGIN
    DECLARE score_sum INTEGER;
    DECLARE weight_sum INTEGER;

    SELECT SUM(projects.weight * corrections.score), 
    SUM(projects.weight) INTO score_sum, weight_sum
    FROM corrections LEFT JOIN projects ON projects.id = corrections.project_id
    WHERE corrections.user_id = p_user_id;

    UPDATE users
    SET average_score = (score_sum / weight_sum)
    WHERE id = p_user_id;
END //
DELIMITER ;