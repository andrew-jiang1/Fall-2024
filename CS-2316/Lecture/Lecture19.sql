use teaching;
# Lecture 19 Example 1 -  Nested Queries
# Use the teaching database to answer the following:
# List the names of all the assistants that have created less than 2 homeworks. 

select creator, count(hw_name) from assistants left join homework on creator = name group by name having count(hw_name) < 2;

# Lecture 19 Example 2 -  Nested Queries
# List all of the students that are older than the average age for a TA. 

select name from assistants where age > (select avg(age) from assistants);

use StudioGhibli;

# Lecture 19 Example 5
# Write a query which gives the film titles and the number of characters in that film for all films directed 
# by Hayao Miyazaki. 

select * from characters c join films f 
on c.title = f.title;

# Lecture 19 -  Coding Exercise
# Write a query that returns the name, age, and gender for all characters that are protagonists and are 
# younger than the average age of all characters combined sorted by ascending age.

# Write a query which gives all the characters’ names in alphabetical order, but only if they were in films 
# that were less than 120 minutes long.

# Write a query that gives the film title and the sum of the ages of all the characters in it for each film 
# that Studio Ghibli has produced. 

select Name,Age,Gender from Characters where (Protagonist = 1) and (age < (select avg(age) from characters)) 
order by age asc;

select name from characters c join films f on c.title = f.title where Duration < 120 order by name;

select title, sum(age) from characters group by title;


