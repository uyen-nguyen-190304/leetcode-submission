-- Write your PostgreSQL query statement below
WITH exam_count_cte AS (
    SELECT
        e.student_id,
        e.subject_name,
        COUNT(*) AS exam_count
    FROM Examinations AS e
    GROUP BY e.student_id, e.subject_name
)

SELECT
    s1.student_id,
    s1.student_name,
    s2.subject_name,
    COALESCE(e.exam_count, 0) AS attended_exams
FROM Students AS s1
CROSS JOIN Subjects AS s2
LEFT JOIN exam_count_cte AS e
    ON s1.student_id = e.student_id AND
       s2.subject_name = e.subject_name
ORDER BY s1.student_id ASC, s2.subject_name ASC;