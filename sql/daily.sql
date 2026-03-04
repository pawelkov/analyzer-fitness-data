SELECT date,
    SUM(calories) AS total_calories
FROM trainings
GROUP BY date
ORDER BY date;
