# Write your MySQL query statement below
SELECT w1.id
FROM Weather AS w1
INNER JOIN Weather AS w2
    # DATEDIFF calculate date1 - date2
    # Thus, this glues current date with previous day if available (?)
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;