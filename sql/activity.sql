SELECT activity_type,
    COUNT(*) AS sessions,
    AVG(calories) AS avg_calories,
    SUM(calories) AS total_calories
FROM trainings
GROUP BY activity_type
ORDER BY total_calories DESC;
