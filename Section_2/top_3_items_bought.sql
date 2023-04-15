SELECT b.item_name, SUM(quantity) AS total_bought
FROM transaction_details a JOIN items b ON a.item_id = b.item_id 
GROUP BY b.item_id
ORDER BY SUM(quantity) DESC
LIMIT 3