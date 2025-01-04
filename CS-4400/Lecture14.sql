use company;
# Write a query that lists the last names of all employees along with a count of how many dependents each has. 

select lname, count(*) from employee left join dependent on ssn = essn group by ssn;

# For each department, retrieve the department number, the number of employees in the department, and their average salary.

select dnumber, count(ssn), avg(salary) from department join employee on dnumber = dno group by dnumber
union
select dnumber,0,0 from department join employee on dnumber = dno group by dnumber having count(ssn) = 0;

select fname,lname from employee join dependent on essn = ssn group by ssn
having count(essn) > 2;

select e.fname,e.lname 
from employee e 
join works_on w on e.ssn = w.essn 
join project p on w.pno = p.pnumber 
where e.dno = 5 and p.pname = "ProjectX" and w.hours > 10;

select * from 
employee as E
join employee as M
on E.superssn = M.ssn


