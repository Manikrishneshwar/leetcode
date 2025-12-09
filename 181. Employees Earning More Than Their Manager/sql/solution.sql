# Write your MySQL query statement below
SELECT EMP.name AS Employee 
FROM Employee AS EMP, Employee AS Manager 
WHERE EMP.managerId=Manager.id 
AND EMP.salary>Manager.salary;