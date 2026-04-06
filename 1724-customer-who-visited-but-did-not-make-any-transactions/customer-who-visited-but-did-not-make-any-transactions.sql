-- Write your PostgreSQL query statement below
SELECT 
    Visits.customer_id,
    SUM(CASE
        WHEN Transactions.transaction_id IS NULL THEN 1
        ELSE 0
    END) AS count_no_trans
FROM Visits 
LEFT JOIN Transactions
    ON Visits.visit_id = Transactions.visit_id
GROUP BY customer_id
HAVING SUM(CASE
        WHEN Transactions.transaction_id IS NULL THEN 1
        ELSE 0
    END) > 0;