/* get selected columns from table */
SELECT first_name,last_name,country 
FROM Customers;

/* get all columns from table */
SELECT * FROM Customers;

/*get varying countries (first instance priority) from table */
SELECT DISTINCT country 
FROM Customers;

/*get the number of instances of varying countries from table */
SELECT COUNT(DISTINCT country) 
FROM Customers;

/*get all columns from table where a data's country has a string value of 'USA'*/
SELECT * FROM Customers 
WHERE country='USA';

/*get all columns from table where the customer ID is odd or not divisble by 2*/
SELECT * FROM Customers 
WHERE customer_id % 2 != 0;

/*Order by defaults: ASC(other term is alphabetical)*/
/*get all columns from table and order by firstname in default ascending order*/
SELECT * FROM Customers
ORDER BY first_name ASC;

/*get all columns from table and order by firstname in descending order*/
SELECT * FROM Customers
ORDER BY first_name DESC;

/*get the 3 columns and sort by country then firstname at descending order*/
SELECT country, first_name, last_name FROM Customers
ORDER BY country ASC, first_name DESC;

/*Strictly select rows where their country is UK and their name starts with J*/
SELECT *
FROM Customers
WHERE Country = 'UK' AND first_name LIKE 'J%';

/*Strictly select rows where their country is UK or their name starts with J*/
SELECT *
FROM Customers
WHERE Country = 'UK' OR first_name LIKE 'J%';

/*get all columns from table where their country is UK and age is 25*/
SELECT * FROM Customers
WHERE country = 'UK'
AND age = '25';

/*combine condition with parenthesis for more specific conditions*/
SELECT * FROM Customers
WHERE (Country = 'UK' OR Country='USA') AND customer_id < 4;

/*get all from table where their country is not 'UAE'*/
SELECT * FROM Customers
WHERE NOT Country = 'UAE';

/*get all from table where their firstname does not start with J*/
SELECT * FROM Customers
WHERE first_name NOT LIKE "J%";

/*get all from table where their customer id does not begin in 1 and end in 3*/
SELECT * FROM Customers
WHERE customer_id NOT BETWEEN 1 AND 3;

/*get all from table where their country is not in UK or USA*/
SELECT * FROM Customers
WHERE country NOT IN ('UK', 'USA');

SELECT * FROM Customers
WHERE NOT customer_id < 2;

/*Insert new row with it's respective column values in order
To insert multiple values/rows, separate with comma and do it again
*/
INSERT INTO Customers (customer_id,first_name, last_name, age, country)
VALUES 
(6,'Liam','Pennyworth','34','IND'),
(7,'Mila','Maui','30','USA');

INSERT INTO Customers (customer_id,first_name, last_name, age, country)
VALUES (NULL,'Liam','Hems','44','IND');

/*To declare a null column, write null without quotation marks*/
SELECT * FROM Customers WHERE customer_id IS NULL;

/*DANGER, IF YOU UPDATE WHERE CONDITION, YOU MIGHT UPDATE ALL VALUE IN TABLE, TRY NOT TO GET FIRED. WHERE ALSO HELPS YOU CHANGE MULTIPLE RECORDS SO USE IT SPARINGLY */
UPDATE Customers 
SET first_name = 'Drew'
WHERE customer_id IS NULL;

/*DANGER, IF YOU DELETE WITHOUT WHERE CONDITION, YOU MIGHT DELETE ALL THE DATA BUT NOT THE TABLE. STILL, BE CAREFUL. WHERE ALSO HELPS YOU CHANGE MULTIPLE RECORDS SO USE IT SPARINGLY*/
DELETE FROM Customers WHERE first_name = "Liam";

/*DANGER, DROP TABLE WILL DELETE ALL YOUR DATA AND THE TABLE WITH IT. USE IT SPARINGLY OR YOU MIGHT GET FIRED*/
DROP TABLE Customers;

SELECT * FROM Customers;

/*WITH SELECT DATABASES, Some use SELECT TOP, LIMIT, FETCH FIRST M ROWS and ROWNUM. Use the specific tools as needed by the database being used*/

/*DATABASE DEPENDENT:limit to 3, might change with conditions*/
SELECT * FROM Customers
LIMIT 3;

/*DATABASE DEPENDENT:fetch first 3, might change with conditions*/
SELECT * FROM Customers
FETCH FIRST 3 ROWS ONLY;

/*Min or Max, selects the highest or lowest value from given column from table*/
SELECT MIN(age)
FROM Customers;

/*AS KEYWORD allows changes to the table heading/title of column */
SELECT MIN(Price) AS SmallestPrice
FROM Products;

/*Gets the youngest persons from each country*/
SELECT MIN(age) AS Youngest_in_each_country , country
FROM Customers
GROUP BY country;

/*displays the count of all the rows/data inside*/
SELECT COUNT(*)
FROM Customers;

/*displays the count of all rows where customer_id column is not null*/
SELECT COUNT(customer_id)
FROM Customers;

/*count distinct countries and name the column*/
SELECT COUNT(DISTINCT country) AS [Number of distinct countries]
FROM Customers;

SELECT COUNT(DISTINCT country) AS [Number of distinct countries]
FROM Customers;

/* Count countries and tally. if you don't add 2nd column, there will be no label */
SELECT COUNT(*) AS [Number of countries], country
FROM Customers
GROUP BY country;

/*Sum of a selected column*/
SELECT SUM(amount)
FROM Orders;

/*Sum of a selected columns with less than 1000 units*/
SELECT SUM(amount) AS [Total Orders]
FROM Orders
WHERE amount < 1000;

/*Sum of selected columns for each item*/
SELECT item, SUM(amount) AS [Total orders per item]
FROM Orders
GROUP BY item;

/*Sum can multiply values ie: SUM(amount * 20) where 20 is shipping costs per item*/
SELECT item, 
SUM(amount) AS [Total orders per item],
SUM(amount * 20) as [Total shipping costs(20 dollars plus)] 
FROM Orders
GROUP BY item;

/*Average per item*/
SELECT item, AVG(amount)
FROM Orders
GROUP BY item;

/*Return products with higher amount than avg*/
SELECT * FROM Orders
WHERE amount > (SELECT AVG(amount) FROM Orders);

/*Wildcard: find the letter in any order*/
SELECT * FROM Customers
WHERE country LIKE '%a%';

/*Wildcard: wild card letters with presets*/
SELECT * FROM Customers
WHERE first_name LIKE 'J__n';

/*Wildcard conditional: find customers either with 'J__n', starts with 'Do%', or ends with '%d'*/
SELECT * FROM Customers
WHERE first_name LIKE 'J__n' OR last_name LIKE 'Do%' OR first_name LIKE '%d';

/*Selects the customers from customer table that are or are not in order table (Relational)*/
SELECT * FROM Customers
WHERE customer_id NOT IN (SELECT customer_id FROM Orders);

/*Select orders with amount between 1 and 1000 and the select items are the ff.*/
SELECT * FROM Orders
WHERE amount BETWEEN 1 AND 1000
AND item IN ("Keyboard","Mouse");

/*Select users between the names alphabetically*/
SELECT * FROM Customers
WHERE first_name BETWEEN 'Betty' AND 'John'
ORDER BY first_name;

/*Between Dates*/
SELECT * FROM Orders
WHERE OrderDate BETWEEN #07/01/1996# AND #07/31/1996#;

SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';

/*Concattinations may work differently on various dbms*/
/*SQL server*/
SELECT customer_id, first_name + ', ' + last_name AS "Fullname"
FROM Customers;

/*MySQL*/
SELECT customer_id, CONCAT(first_name, ', ', last_name) AS "Fullname"
FROM Customers;

/*PostgreSQL*/
SELECT customer_id, first_name || ', ' || last_name AS "Fullname"
FROM Customers;

/*concatinate: postgre for online sql editor*/
SELECT customer_id, first_name || ', ' || last_name AS "Fullname"
FROM Customers;

/*aliasing tables makes it easier to query each of it's column*/
SELECT c.first_name, o.order_id, o.item, o.amount
FROM Customers AS c, Orders as o
WHERE c.customer_id = o.customer_id;

/*Inner Join is modernly explicit in explaining the join*/
SELECT Customers.first_name, Orders.order_id, Orders.item, Orders.amount
FROM Orders
INNER JOIN Customers ON Orders.customer_id=Customers.customer_id;

/*Inner join = finding match in 2 tables*/
/*Left join = return all record in left and the matched record in right*/
/*Left join = return all record in left and the matched record in right*/
/*Full join = return all record when there is match in either left or right*/

/*Inner join: order id and item with shipping status where order id is the same as shipping id*/
SELECT o.order_id, o.item, s.status
FROM Orders as o
INNER JOIN Shippings as s ON o.order_id = s.shipping_id;

/*inner join 3 tables with condition*/
SELECT c.customer_id, o.order_id, o.item, s.status
FROM ((Orders as o
INNER JOIN Customers as c ON c.customer_id = o.customer_id)
INNER JOIN Shippings as s ON (o.order_id = s.shipping_id AND s.status="Pending"));

/*Left join returns all records from the left table (Customers), 
even if there are no matches in the right table (Orders)*/
SELECT Customers.first_name, Orders.order_id
FROM Customers
LEFT JOIN Orders ON Customers.Customer_ID = Orders.Customer_ID
ORDER BY Customers.first_name;

/*The IDE im using doesn't support Right join and Full Join*/

/*Self join: finds pairs that have the same country. This creates duplicate pairs Ex: A - B : S City => B - A : S City*/
SELECT customer_a.first_name AS [1st_customer], customer_b.first_name as [2nd_customer], customer_a.country
FROM Customers AS customer_a, Customers AS customer_b
WHERE customer_a.customer_id <> customer_b.customer_id
AND customer_a.country = customer_b.country
ORDER BY customer_a.country;

/*Find orders and shipping id with the same value: distinct, if you want duplicates use UNION ALL*/
SELECT order_id FROM Orders
UNION
SELECT shipping_id FROM Shippings
ORDER BY order_id;

/*Union with where*/
SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;

/*Another Union example: this example just lists down both supplier and customer*/
SELECT 'Customer' AS Type, ContactName, City, Country
FROM Customers
UNION
SELECT 'Supplier', ContactName, City, Country
FROM Suppliers;

