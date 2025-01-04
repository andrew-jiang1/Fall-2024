use global_company;

select * from employee e join time_frames t on e.ssn = t.ssn where duration > 4 or start_hour > 22;

select distinct pname from project natural join operation_skills
where skill_name like "%data%";

select pname from project p natural join fund_source f group by p.pname having sum(f.usage_rate) > 2000;


CREATE VIEW WORKS_ON1
AS SELECT Fname, Lname, Pname, Hours
FROM EMPLOYEE, PROJECT, WORKS_ON
WHERE Ssn = Essn AND Pno = Pnumber;

# how many employees worked more than 4 hours in a single stretch on a single project

select count(*) from WORKS_ON1 where hours > 4;
