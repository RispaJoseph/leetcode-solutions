# Write your MySQL query statement below
DELETE P1 FROM Person P1
JOIN Person P2 USING(email)
WHERE p1.id>p2.id;
