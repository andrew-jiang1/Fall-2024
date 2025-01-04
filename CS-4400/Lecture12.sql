use company;

select * from employee join department on Dno = Dnumber
where Dname = "Research";

select * from employee join dependent
on ssn = essn;

SELECT * FROM employee right join dependent ON ssn = essn;

# List the project names of projects controlled by departments with a manager who started in 1981.

select * from project join department on dnumber = dnum
where mgrstartdate like  "1981";

# Write a query that lists the last names of all employees that have worked on any project for more than 20 hours.

select * from employee join works_on on ssn = essn where hours > 20;

# Daily Activity

select e.fname, e.lname, p.pname from employee e join works_on w on e.ssn = w.essn right join project p on w.pno = p.pnumber;

# List the names of all employees with two or more dependents.

select lname,fname from employee join dependent
on employee.ssn = dependent.essn
group by employee.ssn having count(dependent_name) >= 2;

# For every project located in 'Stafford', list the project number, the controlling department number, and the department manager's last name, address, and birth date.

select pnumber,dnum,lname,address,bdate from employee join 
	(select * from project join department
	on project.dnum = department.dnumber
	where project.plocation = "Stafford")
as temp
on mgrssn = ssn