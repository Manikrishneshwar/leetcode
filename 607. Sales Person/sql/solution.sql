# Write your MySQL query statement below
SELECT distinct name
FROM SalesPerson
LEFT JOIN Orders ON SalesPerson.sales_id=Orders.sales_id
WHERE SalesPerson.sales_id NOT IN (SELECT sales_ID  FROM Orders
LEFT JOIN Company ON Orders.com_id=Company.com_id WHERE Orders.com_id=(SELECT com_ID FROM Company WHERE name='RED'))
OR Orders.sales_id iS NULL
