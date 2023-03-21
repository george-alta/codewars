SELECT p.id, p.name, count(s.sale) AS sale_count, RANK() OVER (ORDER BY SUM(s.price) DESC) AS sale_rank
FROM people as p
JOIN sales as s ON s.people_id = p.id
GROUP BY p.id
