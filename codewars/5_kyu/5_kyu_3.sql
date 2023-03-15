SELECT DATE(created_at) AS day, description, COUNT(*)
FROM events
WHERE name = 'trained'
GROUP BY DATE(created_at), description