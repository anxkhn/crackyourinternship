SELECT author_id AS id 
FROM views 
WHERE author_id = viewer_id 
GROUP BY id 
ORDER BY id ASC;
