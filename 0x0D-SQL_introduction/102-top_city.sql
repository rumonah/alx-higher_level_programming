-- displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
CREATE TABLE IF NOT EXISTS temp_july_augu SELECT * FROM temperatures
WHERE months = 7 or month = 8;
SELECT city, AVG(value) AS avg_temp FROM temp_july_augu GROUP BY city ORDER BY avg_temp DESC limit 3;
