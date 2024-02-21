-- script that lists the number of records with the same score in the table
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY SCORE
ORDER BY SCORE DESC;
