-- Write your PostgreSQL query statement below
SELECT e.name
FROM (
    SELECT
        e1.id,
        COUNT(*) AS report_count
    FROM Employee AS e1
    INNER JOIN Employee AS e2
        ON e1.id = e2.managerID
    GROUP BY e1.id
) AS reports
LEFT JOIN Employee AS e
    ON reports.id = e.id
WHERE reports.report_count >= 5;