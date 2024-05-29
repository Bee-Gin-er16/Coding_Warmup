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

/*AS KEYWORD allows changes to the table heading/title */
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