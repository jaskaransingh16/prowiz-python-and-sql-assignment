-- second topper in the class 
SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 1 OFFSET 1;

-- The second topper in class. If 2 candidates have same marks then the one with their name first in
-- alphabetical order is given the better(lower) rank

SELECT name, marks
FROM students
ORDER BY marks DESC, name ASC
LIMIT 1 OFFSET 1;

-- The second topper(s) in class. If multiple candidates have same marks, they are given the same rank, so
-- multiple individuals can have rank 1.

SELECT name, marks
FROM (
    SELECT name, marks,
           DENSE_RANK() OVER (ORDER BY marks DESC) AS rnk
    FROM students
) t
WHERE rnk = 2;