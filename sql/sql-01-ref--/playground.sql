CREATE TABLE authors (
	author_name VARCHAR(60),
	author_email VARCHAR(70),
	author_pay int
)

INSERT INTO authors (author_name, author_email, author_pay)
VALUES ('Fred Jones', 'fred2jones@gmail.com', 65000)
INSERT INTO authors (author_name, author_email, author_pay)
VALUES ('Samantha Troy', 'sammy_h_troy@gmail.com', 65000)
INSERT INTO authors (author_name, author_email, author_pay)
VALUES ('Lyra Liao', 'lyrazliao@gmail.com', 164000)

SELECT author_name,
	author_email
FROM authors
GROUP BY author_pay
ORDER BY author_pay DESC
LIMIT 1

WITH summary AS (
    SELECT a.author_name, 
           a.author_email, 
           a.author_pay, 
           ROW_NUMBER() OVER(PARTITION BY a.author_pay
                                 ORDER BY a.author_name DESC) AS row
      FROM authors a)
SELECT s.*
  FROM summary s
 WHERE s.row = 1