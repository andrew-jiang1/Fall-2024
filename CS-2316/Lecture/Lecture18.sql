# Lecture 18 Example 1 
# Using the teaching database, write a sql query that gives the name and age of the second oldest student 
# that has an a or an e in their name.

use teaching;

select name,age from assistants where name like '%a%' or name like '%e%' 
order by age desc limit 1 offset 1;


# Lecture 18 Example 1.5
# list the names and ages of all the assistants who are older than the average age

select name, age from assistants where age > (select avg(age) from assistants);

# Lecture 18 Example 2
# Using the teaching database, write an sql query that lists the names and ages of the the assistants
#  who are between 20 and 22 years old (inclusive) and whose name not does contain the letter T.

select name, age from assistants where age between 20 and 22 and name not like '%t%';

# Lecture 18 Example 3
# Using the teaching database, write a sql query returning the name and how many homeworks each TA has created 
# sorted DESCENDING by number of homeworks.

select name, count(h.hw_name) numhw from assistants a join homework h on a.name = h.creator group by a.name order by count(h.hw_name) desc;

# Lecture 18 Example 4
# Using the teaching database, write a sql query that lists the oldest age of a TA who has never created a 
# homework assignment. 

select max(age) from assistants left join homework on name = creator 
where hw_name is null;

select count(hw_name) from assistants join homework on name = creator where age < 21;
select hw_name from assistants join homework on name = creator where year = 2;
select avg(age) from assistants right join homework on name = creator;
select hw_name, creator from homework left join assistants on creator = name order by age;


