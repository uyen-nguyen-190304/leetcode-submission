-- Write your PostgreSQL query statement below
SELECT 
    EmployeeUNI.unique_id,
    Employees.name
FROM Employees
FULL OUTER JOIN EmployeeUNI
    ON Employees.id = EmployeeUNI.id
WHERE Employees.name IS NOT NULL;