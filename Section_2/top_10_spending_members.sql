SELECT member_id, SUM(total_price) AS spending
FROM transactions
GROUP BY member_id
ORDER BY SUM(total_price) DESC
LIMIT 10