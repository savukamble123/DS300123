use product;
-- 1.Count the number of Salesperson whose name begin with ‘a’/’A’.

select count(sname) as Count from salespeople where sname like 'a%' or sname like 'A%';

-- 2.Display all the Salesperson whose all orders worth is more than Rs. 2000.

SELECT S.snum ,S.sname
FROM SalesPeople S
JOIN Orders O ON S.snum = O.snum
GROUP BY S.snum, S.sname
HAVING SUM(O.Amt) > 2000;

-- 3. Count the number of Salesperson belonging to Newyork.

select count(sname) from salespeople where city like '%Newyork%';


-- 4.Display the number of Salespeople belonging to London and belonging to Paris.

select sname from salespeople where city like '%London%' or city like '%Paris%';

-- 5.Display the number of orders taken by each Salesperson and their date of orders.

SELECT S.Snum, S.Sname, COUNT(O.Onum) AS OrderCount, GROUP_CONCAT(O.Odate SEPARATOR ', ') AS OrderDates
FROM SalesPeople S
LEFT JOIN Orders O ON S.Snum = O.Snum
GROUP BY S.Snum, S.Sname;

