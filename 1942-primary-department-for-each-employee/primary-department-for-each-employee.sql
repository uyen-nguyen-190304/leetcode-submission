-- Write your PostgreSQL query statement below
SELECT
    e1.employee_id,
    CASE 
        WHEN COUNT(*) = 1 THEN (
            SELECT e2.department_id 
            FROM Employee AS e2
            WHERE e1.employee_id = e2.employee_id
        )
        ELSE (
            SELECT e3.department_id 
            FROM Employee AS e3 
            WHERE e1.employee_id = e3.employee_id 
                AND e3.primary_flag = 'Y'
        )
    END AS department_id
FROM Employee AS e1
GROUP BY e1.employee_id;