use company;
select * from employee where salary > 30000;
select * from employee where fname like '_r%';
select bdate, Address from employee where fname = "John" and lname = "Smith";
select fname,lname from employee order by lname desc;

SELECT E.Fname, E.Lname, S.Fname, S.Lname
FROM EMPLOYEE AS E, EMPLOYEE AS S
WHERE E.Superssn = S.Ssn;

select lname from employee where lname like "_e";
select lname, address, salary from employee where salary > 40000 and address like '%b%' or '%d%';
select lname, fname, bdate from employee order by bdate desc;
select lname, salary*1.05 from employee order by salary desc;

SELECT DISTINCT Essn
FROM WORKS_ON
WHERE Pno IN (1, 2, 3);

SELECT CONCAT(lname, ', ', fname) AS full_name
FROM EMPLOYEE;

SELECT ROUND(salary * 1.05, 1) AS 'New Salary'
FROM EMPLOYEE;

SELECT avg (salary)
FROM Employee WHERE fname like 'j%';

SELECT Dno, AVG(salary)
FROM EMPLOYEE
GROUP BY Dno;

SELECT Dno,AVG(salary)
FROM EMPLOYEE
GROUP BY Dno HAVING Dno > 4;



