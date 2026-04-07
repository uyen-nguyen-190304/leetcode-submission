-- Write your PostgreSQL query statement below
SELECT 
    e3.employee_id,
    e4.name,
    e3.reports_count,
    e3.average_age
FROM (
    SELECT
        e1.employee_id,
        COUNT(*) AS reports_count,
        ROUND(AVG(e2.age)) AS average_age
    FROM Employees AS e1
    INNER JOIN Employees AS e2
        ON e1.employee_id = e2.reports_to
    GROUP BY e1.employee_id
) AS e3
INNER JOIN Employees AS e4
    ON e3.employee_id = e4.employee_id
ORDER BY e3.employee_id ASC;