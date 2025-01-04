drop database if exists teaching;
create database teaching;
use teaching;
create table assistants (name varchar(100), age int, year int);
insert into assistants (name,age,year) values ('Anna',20,2);
insert into assistants (name,age,year) values ('Liv',21,4);
insert into assistants (name,age,year) values ('Madison',22,4);
insert into assistants (name,age,year) values ('Jacob',21,3);	
insert into assistants (name,age,year) values ('Ashok',21,1);	
insert into assistants (name,age,year) values ('Athena',20,2);	

create table homework (hw_name varchar(4), creator varchar(100));
insert into homework (hw_name,creator) values ('HW01', 'Jacob');
insert into homework (hw_name,creator) values ('HW02', 'Jacob');
insert into homework (hw_name,creator) values ('HW03','Athena');
insert into homework (hw_name,creator) values ('HW04','Anna');	
insert into homework (hw_name,creator) values ('HW05','Anna');	
insert into homework (hw_name,creator) values ('Lab1','Ashok');	


select count(*) from assistants where name like '%a';
select name from assistants where year = 2;
select min(age) from assistants where year = 3;
select avg(age), year from assistants group by year;