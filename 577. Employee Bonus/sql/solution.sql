# Write your MySQL query statement below
SELECT emp.name, Bonus.bonus 
FROM Employee AS emp
LEFT JOIN Bonus ON emp.empId=Bonus.empId
WHERE  Bonus.bonus IS NULL
OR Bonus.bonus <1000;