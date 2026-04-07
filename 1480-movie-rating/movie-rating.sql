-- Write your PostgreSQL query statement below
(
    SELECT Users.name AS results
    FROM (
        SELECT
            user_id,
            COUNT(*) AS rating_count
        FROM MovieRating
        GROUP BY user_id
    ) AS MovieRatingCount
    LEFT JOIN Users
        ON MovieRatingCount.user_id = Users.user_id
    ORDER BY MovieRatingCount.rating_count DESC, Users.name ASC
    LIMIT 1
)

UNION ALL

(
    SELECT Movies.title AS results
    FROM (
        SELECT
            movie_id,
            AVG(rating) AS average_rating
        FROM MovieRating
        WHERE created_at >= '2020-02-01' AND created_at < '2020-03-01' 
        GROUP BY movie_id
    ) AS MovieRatingAverage
    LEFT JOIN Movies
        ON MovieRatingAverage.movie_id = Movies.movie_id
    ORDER BY MovieRatingAverage.average_rating DESC, Movies.title ASC
    LIMIT 1
)
