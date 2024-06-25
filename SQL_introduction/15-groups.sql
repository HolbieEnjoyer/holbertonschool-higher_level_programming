-- bashi
SELECT DISTINCT score, COUNT(score) AS number
FROM second_table
ORDER BY number DESC;