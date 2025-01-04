DROP DATABASE IF EXISTS StudioGhibli;
CREATE DATABASE StudioGhibli;
USE StudioGhibli;


CREATE TABLE Films(
	Title varchar(75) PRIMARY KEY, 
	Director varchar(30),
	Rating varchar(10),
	Duration int,
	ReleaseDate int
);

CREATE TABLE Characters(
	Title varchar(75), 
	Name varchar(30),
	Gender varchar(30),
	Age int,
	Protagonist int
);

INSERT INTO Films (Title, Director, Rating, Duration, ReleaseDate) VALUES ('Grave of the Fireflies', 'Isao Takahata', 'PG', 88, 1988);
INSERT INTO Films (Title, Director, Rating, Duration, ReleaseDate) VALUES ('Howl\'s Moving Castle', 'Hayao Miyazaki', 'G', 119, 2004);
INSERT INTO Films (Title, Director, Rating, Duration, ReleaseDate) VALUES ('Kiki\'s Delivery Service', 'Hayao Miyazaki', 'G', 103, 1989);
INSERT INTO Films (Title, Director, Rating, Duration, ReleaseDate) VALUES ('My Neighbor Totoro', 'Hayao Miyazaki', 'G', 86, 1988);
INSERT INTO Films (Title, Director, Rating, Duration, ReleaseDate) VALUES ('Princess Mononoke', 'Hayao Miyazaki', 'PG-13', 133, 1997);
INSERT INTO Films (Title, Director, Rating, Duration, ReleaseDate) VALUES ('Spirited Away', 'Hayao Miyazaki', 'G', 125, 2001);

INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Howl\'s Moving Castle', 'Sophie Hatter', 'F', 18, 1);
INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Howl\'s Moving Castle', 'Howl', 'M', 27, 0);
INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Howl\'s Moving Castle', 'Calcifer', NULL, NULL, 0);
INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Howl\'s Moving Castle', 'Markl', 'M', 15, 0);

INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('My Neighbor Totoro', 'Satsuki', 'F', 11, 1);
INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('My Neighbor Totoro', 'Mei', 'F', 4, 0);
INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('My Neighbor Totoro', 'Totoro', NULL, NULL, 1);

INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Kiki\'s Delivery Service', 'Kiki', 'F', 13, 1);
INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Kiki\'s Delivery Service', 'Jiji', 'F', NULL, 0);
INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Kiki\'s Delivery Service', 'Tombo', 'M', 13, 0);

INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Spirited Away', 'Chihiro Ogino (Sen)', 'F', 10, 1);
INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Spirited Away', 'Haku', 'M', 12, 0);
INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Spirited Away', 'Kaonashi', NULL, NULL, 0);

INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Princess Mononoke', 'Ashitaka', 'M', 17, 1);
INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Princess Mononoke', 'San', 'F', 15, 0);

INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Grave of the Fireflies', 'Seita', 'M', 14, 1);
INSERT INTO Characters (Title, Name, Gender, Age, Protagonist) VALUES ('Grave of the Fireflies', 'Setsuko', 'F', 4, 0);