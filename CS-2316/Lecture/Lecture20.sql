Drop database if exists hogwarts;
Create database hogwarts;
Use hogwarts;

create table classes 
	(c_name varchar(30), 
	 enrollment int, 
	 teacher varchar(40),
       FOREIGN KEY (teacher) REFERENCES professors (p_name));

create table professors 
	(p_name varchar(40),
	 house enum('slytherin','hufflepuff',
	 	         'ravenclaw','gryffindor'));	

create table students 
	(s_name varchar(40), 
	 house enum('slytherin','hufflepuff',
	 	         'ravenclaw','gryffindor'),
       PRIMARY KEY (s_name)
     );


create table sports
	(game varchar(40),
    equipment varchar(40), 
    player varchar(40));
                 
insert into students (s_name) values ('harry potter');
insert into students values ('ron weasley', 'gryffindor');
insert into classes values ('potions',20,'snape');
insert into professors values ('snape','slytherin');
insert into professors values ('mcgonagall','gryffindor');

update students set house = 'gryffindor' where house is null;
UPDATE classes SET enrollment = 0 where teacher = 'snape';
UPDATE students SET s_name='Harry Potter' where s_name LIKE 'h%';

insert into sports values ('Broomball','broomstick',null);
update sports set game = 'Quidditch' where game like 'Broomball';
insert into sports values ('Mumblypeg','knife',null);
delete from sports where equipment like 'knife';
update sports set player = 'Harry Potter' where game like 'Quidditch';

select game from sports s join students st on s.player = st.s_name where st.house like 'gryffindor'; 






DELETE FROM classes where enrollment < 5;
insert into classes values ('potions',5,'snape');








