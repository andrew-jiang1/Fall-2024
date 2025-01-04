Drop Database if exists CS2316;
Create Database CS2316;
Use CS2316;
drop table if exists students;
create table students
(fname varchar(64),
lname varchar(64),
age int);

insert into students (fname,lname,age) values ('Athena', 'Malek', 21);
insert into students (fname,lname,age) values ('Brandone','Vo',22);
insert into students (fname,lname,age) values ('Anna','Zhao',20);
insert into students (fname,lname,age) values ('Christine','Ling',21);
insert into students (fname,lname,age) values ('Sami','Mathew',20);
insert into students (fname,lname,age) values ('Jeremy','Thomas',20);
select * from students;

update students set age = 21 where fname = 'Brandone';

select fname, age from students where fname = 'Sami';
select fname, age + 5 from students where fname = 'Jeremy';

select * from students where fname like 'b%';

select * from students order by age desc;

select * from students order by age desc, lname desc;