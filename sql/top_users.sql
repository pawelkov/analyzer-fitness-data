SELECT user_id,
    COUNT(*) AS sessions,
    SUM(calories) AS total_calories
FROM trainings
GROUP BY user_id
ORDER BY total_calories DESC
LIMIT 5;
