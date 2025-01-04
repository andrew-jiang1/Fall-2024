-- CS4400: Introduction to Database Systems (Fall 2024)
-- Phase II: Create Table & Insert Statements [v0] Monday, September 15, 2024 @ 17:00 EST

-- Team __
-- Andrew Jiang (ajiang70)
-- Andy Vo (avo46)
-- Kelly Zhang (kzhang467)
-- Leo Zheng (lzheng305)

-- Directions:
-- Please follow all instructions for Phase II as listed on Canvas.
-- Fill in the team number and names and GT usernames for all members above.
-- Create Table statements must be manually written, not taken from an SQL Dump file.
-- This file must run without error for credit.

/* This is a standard preamble for most of our scripts.  The intent is to establish
a consistent environment for the database behavior. */
set global transaction isolation level serializable;
set global SQL_MODE = 'ANSI,TRADITIONAL';
set names utf8mb4;
set SQL_SAFE_UPDATES = 0;

set @thisDatabase = 'business_supply';
drop database if exists business_supply;
create database if not exists business_supply;
use business_supply;

-- Define the database structures
/* You must enter your tables definitions, along with your primary, unique and foreign key
declarations, and data insertion statements here.  You may sequence them in any order that
works for you.  When executed, your statements must create a functional database that contains
all of the data, and supports as many of the constraints as reasonably possible. */
# Unique: taxID, ID, tag, warehouse skill(?)
# Unique: taxID, ID, tag, warehouse skill(?)
CREATE TABLE user(
username varchar(40) not null,  # key att = 40 
first_name varchar(100) not null, # first & last name = 100
last_name varchar(100) not null, 
address varchar(500) not null, # address = 500
birthday date,
	PRIMARY KEY(username)
);
INSERT INTO user VALUES
('agarcia7','Alejandro','Garcia','710 Living Water Drive','1966-10-29'),
('awilson5','Aaron','Wilson','220 Peachtree Street','1963-11-11'),
('bsummers4','Brie','Summers','5105 Dragon Star Circle','1976-02-09'),
('cjordan5','Clark','Jordan','77 Infinite Stars Road','1966-06-05'),
('ckann5','Carrot','Kann','64 Knights Square Trail','1972-09-01'),
('csoares8','Claire','Soares','706 Living Stone Way','1965-09-03'),
('echarles19','Ella','Charles','22 Peachtree Street','1974-05-06'),
('eross10','Erica','Ross','22 Peachtree Street','1975-04-02'),
('fprefontaine6','Ford','Prefontaine','10 Hitch Hikers Lane','1961-01-28'),
('hstark16','Harmon','Stark','53 Tanker Top Lane','1971-10-27'),
('jstone5','Jared','Stone','101 Five Finger Way','1961-01-06'),
('lrodriguez5','Lina','Rodriguez','360 Corkscrew Circle','1975-04-02'),
('mrobot1','Mister','Robot','10 Autonomy Trace','1988-11-02'),
('mrobot2','Mister','Robot','10 Clone Me Circle','1988-11-02'),
('rlopez6','Radish','Lopez','8 Queens Route','1999-09-03'),
('sprince6','Sarah','Prince','22 Peachtree Street','1968-06-15'),
('tmccall5','Trey','McCall','360 Corkscrew Circle','1973-03-19'); 


#employee(username[FK1],taxID, experience, salary,hired)
	#FK1: username → user(username)
CREATE TABLE employee(
username varchar(40) not null, 
taxID varchar(11) unique, # key in xxx-xx-xxxx format 
experience int, # default = 100
salary int,
hired date,
PRIMARY KEY (username, taxID),
FOREIGN KEY (username) REFERENCES user(username)
) ;
INSERT INTO employee VALUES
('agarcia7', '999-99-9999', 24, 41000, '2019-03-17'),
('awilson5', '111-11-1111', 9, 46000, '2020-03-15'),
('bsummers4', '000-00-0000', 17, 35000, '2018-12-06'),
('ckann5', '640-81-2357' ,27, 46000, '2019-08-03'),
('csoares8', '888-88-8888', 26, 57000, '2019-02-25'),
('echarles19', '777-77-7777', 3, 27000, '2021-01-02'),
('eross10', '444-44-4444', 10, 61000, '2020-04-17'),
('fprefontaine6', '121-21-2121', 5, 20000, '2020-04-19'),
('hstark16', '555-55-5555', 20, 59000, '2018-07-23'),
('lrodriguez5', '222-22-2222', 20, 58000, '2019-04-15'),
('mrobot1', '101-01-0101', 8, 38000, '2015-05-27'),
('mrobot2', '010-10-1010', 8, 38000, '2015-05-27'),
('rlopez6', '123-58-1321', 51, 64000, '2017-02-05'),
('tmccall5', '333-33-3333', 29, 33000, '2018-10-17');

#owner(username[FK2])
	#FK2: username → user(username)
CREATE TABLE owner(
	username varchar(40) not null,
	PRIMARY KEY(username),
	FOREIGN KEY (username) REFERENCES user(username)
) ;
INSERT INTO owner VALUES
('cjordan5'),
('jstone5'),
('sprince6');

#driver(username[FK3], taxID[FK4], licenseID,license_type, successful_trips)
	#FK3: username → user(username)
	#FK4: taxID → employee(taxID)
CREATE TABLE driver(
username varchar(40) not null,
licenseID varchar(40) not null, 
license_type varchar(100) not null, 
successful_trips int not null,
taxID varchar(11) not null,
PRIMARY KEY (username, taxID, licenseID),
FOREIGN KEY (username) REFERENCES user(username),
FOREIGN KEY (taxID) REFERENCES employee(taxID)
) ;
INSERT INTO driver VALUES
('agarcia7', '610623', 'CDL', 38, '999-99-9999'),
('awilson5', '314159', 'commercial', 41, '111-11-1111'),
('bsummers4', '411911', 'private', 35, '000-00-0000'),
('csoares8', '343563', 'commericial', 7, '888-88-8888'),
('fprefontaine6', '657483', 'private', 2, '121-21-2121'),
('lrodriguez5', '287182', 'CDL', 67, '222-22-2222'),
('mrobot1', '101010', 'CDL', 18, '101-01-0101'),
('rlopez6', '235711', 'private', 58, '123-58-1321');

#worker(username[FK5], taxID[FK6] , managesserviceID)
	#FK5: username → user(username)
	#FK6: taxID → employee(taxID)
CREATE TABLE worker(
username varchar(40) not null,
taxID varchar(11) not null,
PRIMARY KEY (username, taxID),
FOREIGN KEY (username) REFERENCES user(username),
FOREIGN KEY (taxID) REFERENCES employee(taxID)
) ;
INSERT INTO worker VALUES
('ckann5','640-81-2357'),
('echarles19','777-77-7777'),
('eross10','444-44-4444'),
('hstark16','555-55-5555'),
('mrobot2','010-10-1010');

#business(name, spent,rating)
CREATE TABLE business(
name varchar(40) not null,
rating int not null,
spent int not null,
CHECK (rating between 1 and 5),
PRIMARY KEY (name)
) ;

INSERT INTO business VALUES
('Aircraft Electrical Svc', 5, 10),
('Homestead Insurance', 5, 30),
('Jones and Associates', 3, 0),
('Prime Solutions', 4, 30),
('Innovative Ventures', 4, 0),
('Blue Horizon Enterprises', 4, 10),
('Peak Performance Group', 5, 20),
('Summit Strategies', 2, 0),
('Elevate Consulting', 5, 30),
('Pinnacle Partners', 4, 10);

#service(ID, name)
CREATE TABLE service(
ID varchar(40) not null unique,
name varchar(100) not null,
managedby varchar(40) not null,
PRIMARY KEY (ID),
FOREIGN KEY (managedby) REFERENCES worker(username)
) ;
INSERT INTO service VALUES
('mbm','Metro Business Movers','hstark16'),
('lcc','Local Commerce Couriers','eross10'),
('pbl','Pro Business Logistics','echarles19');



#location(bname[FK7], sID[FK8], label, x_coord, y_coord, space)
	#FK7: bname → business(name)
	#FK8: sID → service(ID)
CREATE TABLE location(
bname varchar(40),
sID varchar(40),
space varchar(100),
x_coord varchar(100) not null,
y_coord varchar(100) not null,
label varchar(40) not null,
PRIMARY KEY (label,bname),
FOREIGN KEY (bname) REFERENCES business(name),
FOREIGN KEY (sID) REFERENCES service(ID)
) ;

INSERT INTO location VALUES
('Aircraft Electrical Svc', NULL, '15', '5' ,'-6', 'airport'),
('Homestead Insurance', NULL, '10', '-4', '-3', 'downtown'),
('Jones and Associates', NULL, '8', '7', '10', 'springs'),
('Prime Solutions', NULL, '8', '7', '10', 'buckhead'),
('Innovative Ventures', 'pbl', '12', '2', '15', 'avalon'),
('Blue Horizon Enterprises', NULL,NULL, '-8', '5', 'mercedes'),
('Peak Performance Group', NULL,'7', '2', '1', 'highlands'),
('Summit Strategies', 'mbm', '5', '1', '-16', 'southside'),
('Elevate Consulting', NULL, '7', '2', '1', 'midtown'),
('Pinnacle Partners', 'lcc', '10', '-4', '-3', 'plaza');






#product(barcode, iname, weight)
CREATE TABLE product(
barcode varchar(40) not null,
iname varchar(100) not null,
weight int not null, # in lb
	PRIMARY KEY (barcode)
) ;
INSERT INTO product VALUES
('gc_4C6B9R', 'glass cleaner', '4'),
('pn_2D7Z6C', 'pens', '5'),
('sd_6J5S8H', 'screwdrivers', '4'),
('st_2D4E6L', 'shipping tape', '3'),
('hm_5E7L23M', 'hammer', '3');



#van(sID[FK11], tag, label[FK9], bname[FK10], dusername[FK12], fuel, capacity, sales)
	#FK9: label → location(label)
	#FK10: bname →  business(name)
	#FK11: sID → service(ID)
	#FK12: dusername → driver(username)
CREATE TABLE van(
	sID varchar(40) not null,
	tag int not null,
	fuel int not null,
	capacity int not null,
	sales int not null,
	dusername varchar(40),
	label varchar(40) not null,
	PRIMARY KEY (tag, sID),
	FOREIGN KEY (sID) REFERENCES service(ID),
	FOREIGN KEY (label) REFERENCES location(label),
	FOREIGN KEY (dusername) REFERENCES user(username)
);
INSERT INTO van VALUES
('mbm', 1, 100, 6, 0, 'fprefontaine6', 'southside'),
('mbm', 5, 27, 7, 100, 'fprefontaine6', 'buckhead'),
('mbm', 8, 100, 8, 0, 'bsummers4', 'southside'),
('mbm', 11, 25, 10, 0, NULL, 'southside'),
('mbm', 16, 17, 5, 40, 'fprefontaine6', 'southside'),
('lcc', 1, 100, 9, 0, 'awilson5', 'airport'),
('lcc', 2, 75, 7, 0, NULL, 'plaza'),
('pbl', 3, 100, 5, 50, 'agarcia7', 'avalon'),
('pbl', 7, 53, 5, 100, 'agarcia7', 'avalon'),
('pbl', 8, 100, 6, 0, 'agarcia7', 'highlands'),
('pbl', 11, 90, 6, 0, NULL, 'avalon');


#fund(username[FK13], bname[FK14], invested, date)
	#FK13: username → user(username)
	#FK14: bname → business(name) 
CREATE TABLE fund(
username varchar(40) not null,
bname varchar(40) not null,
invested int not null,
date date not null,
PRIMARY KEY (username, bname),
FOREIGN KEY (username) REFERENCES user(username),
FOREIGN KEY (bname) REFERENCES business(name)
) ;
INSERT INTO fund VALUES
('jstone5', 'Jones and Associates', 20, '2022-10-25'),
('sprince6', 'Blue Horizon Enterprises', 10, '2022-03-06'),
('jstone5', 'Peak Performance Group', 30, '2022-09-08'),
('jstone5', 'Elevate Consulting', 5, '2022-07-25');

#contain(sID[FK15], tag[FK16], pbarcode[FK17], price, quantity)
	#FK15: sID → service(ID)
	#FK16: tag → van(tag)
CREATE TABLE contain( 
pbarcode varchar(100) not null,
sID varchar(40) not null,
tag int not null,
quantity varchar(100) not null,
price varchar(100) not null,
PRIMARY KEY (sID, tag),
FOREIGN KEY (sID) REFERENCES service(ID),
FOREIGN KEY (tag) REFERENCES van(tag),
FOREIGN KEY (pbarcode) REFERENCES product(barcode)
) ;
INSERT INTO contain VALUES
('pn_2D7Z6C', 'pbl', 3, '2', '28'),
('pn_2D7Z6C', 'mbm', 5, '1', '30'),
('st_2D4E6L', 'lcc', 1, '3', '23'),
('st_2D4E6L', 'mbm', 11, '3', '19'),
('st_2D4E6L', 'mbm', 1, '6', '27'),
('hm_5E7L23M', 'lcc', 2, '7', '14');


#work_for(sID [FK18], username, taxID[FK19])
	#FK18: sID → service(ID)
	#FK19: username, taxID → worker(username, taxID)
CREATE TABLE work_for(
	sID varchar(40) not null,
	username varchar(40) not null,
	taxID varchar(11) not null,
	PRIMARY KEY (sID, username, taxID),
	FOREIGN KEY (sID) REFERENCES service(ID),
	FOREIGN KEY (taxID) REFERENCES employee(taxID)
);
INSERT INTO work_for VALUES
('lcc', 'ckann5', '640-81-2357'),
('pbl', 'echarles19', '777-77-7777'),
('lcc', 'eross10', '444-44-4444'),
('mbm', 'hstark16', '555-55-5555'),
('mbm', 'tmccall5', '333-33-3333'),
('pbl', 'mrobot2', '010-10-1010');


