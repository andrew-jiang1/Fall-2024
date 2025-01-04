use company;
-- # write a function that takes in a first name and a last name and returns the concatenation of them together with a space in between.

-- drop function if exists get_combined_name;
-- delimiter //

-- create function get_combined_name(lname char(10), fname char(20))
-- returns char(31) deterministic
-- begin
--     return concat(fname, '  ', lname);
-- end //
-- delimiter ; # set delimiter back to the ;

-- select get_combined_name(fname,lname) from employee;


-- -- Write a function called second_highest returns the second highest salary of an employee in the company 
-- -- database that works for a particular department.
-- drop function if exists second_highest;
-- delimiter //
-- create function second_highest (in_dno decimal(1,0))
-- returns decimal(5,0) deterministic
-- begin
--    declare second_spot decimal(5,0);
--    select salary into second_spot from employee where dno = in_dno
--    order by salary desc limit 1 offset 1;
--    return second_spot;
-- end //
-- delimiter ;

-- select second_highest(5);

  
# Test your function using the following statement:
#select second_highest(5);

-- Write a stored procedure called insert_if_ok that inserts a record into the 
-- works_on table of the company database only if the hours are not more than 20

drop procedure if exists insert_if_ok;
delimiter //
create procedure insert_if_ok (in_ssn decimal(9,0),  in_proj decimal(2,0), in_hours decimal(5,1))
begin
    if in_hours <= 20 then
         insert into works_on values(in_ssn, in_proj, in_hours);
	end if;
end //
delimiter ;


#Test your code by using these two procedure calls then looking at the works_on table to see the results:
call insert_if_ok(999999999,5,10); # should enter a new row
call insert_if_ok(123456789,5,30); #should have no effect

-- Write a stored procedure called update_project that changes the row in the works_on table from one project 
# number to another number

drop procedure if exists update_project;
delimiter //
create procedure update_project (in_oldproj decimal(2,0),  in_new_proj decimal(2,0))
sp_main: begin
    if not in_oldproj in (select pnumber from project) then select 'curr project number not in works_on';leave sp_main;end if;
    if in_oldproj in (select pno from works_on) then select 'current project number is being used in the works_on table'; leave sp_main; end if;
    if in_new_proj in (select pnumber from project) then select 'new proj number already in project label' ; leave sp_main; end if;
    update project set pnumber = in_new_proj where pnumber = in_oldproj;
end //
delimiter ;

call update_project(4,5); 

insert into project values ('Project4400',4,'Atlanta',1);
