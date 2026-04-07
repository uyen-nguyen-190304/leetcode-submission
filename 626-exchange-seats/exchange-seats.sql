-- Write your PostgreSQL query statement below
SELECT
    id,
    CASE 
        WHEN id = (SELECT MAX(id) FROM Seat) and id % 2 = 1 THEN student
        WHEN id % 2 = 1 THEN (SELECT student FROM Seat AS s2 WHERE s2.id = s1.id + 1)
        WHEN id % 2 = 0 THEN (SELECT student FROM Seat AS s2 WHERE s2.id = s1.id - 1) 
    END AS student
FROM Seat AS s1
ORDER BY id ASC;