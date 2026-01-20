# Write your MySQL query statement below
SELECT *
FROM  Cinema
WHERE description!="boring"
AND id&1!=0 
ORDER BY rating DESC