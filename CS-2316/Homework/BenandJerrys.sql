DROP DATABASE IF EXISTS BenAndJerrys;
CREATE DATABASE BenAndJerrys;
USE BenAndJerrys;

CREATE TABLE Celebrities (
    CelebID INT PRIMARY KEY,
    CelebName VARCHAR(255) NOT NULL,
    Occupation VARCHAR(255) NOT NULL
);

CREATE TABLE IceCreamInfo (
    IcecreamID INT PRIMARY KEY,
    FullName VARCHAR(255) NOT NULL,
    YearCreated INT,
    CelebrityID INT,
    FOREIGN KEY (CelebrityID) REFERENCES Celebrities(CelebID) ON DELETE SET NULL
);

CREATE TABLE KrogerAvailability (
    KrogerID INT PRIMARY KEY,
    IcecreamID INT,
    FullName VARCHAR(255) NOT NULL,
    PintsInStock INT,
    LastMonthOrdered VARCHAR(50),
    NextMonthOrder VARCHAR(50),
    FOREIGN KEY (IcecreamID) REFERENCES IceCreamInfo(IcecreamID)
);


INSERT INTO Celebrities (CelebID, CelebName, Occupation)
VALUES 
(101, 'Stephen Colbert', 'TV Host'),
(102, 'Jimmy Fallon', 'TV Host'),
(103, 'Jerry Garcia', 'Musician'),
(104, 'John Lennon', 'Musician'),
(105, 'Bob Marley', 'Musician'),
(106, 'Phish', 'Band'),
(108, 'Dave Matthews', 'Musician');


INSERT INTO IceCreamInfo (IcecreamID, FullName, YearCreated, CelebrityID)
VALUES 
(1, 'Americone Dream', 2007, 101),    -- Stephen Colbert
(2, 'Tonight Dough', 2015, 102),      -- Jimmy Fallon
(3, 'Cherry Garcia', 1987, 103),      -- Jerry Garcia
(4, 'Imagine Whirled Peace', 2008, 104), -- John Lennon
(5, 'Bob Marley’s One Love', 2016, 105), -- Bob Marley
(6, 'Phish Food', 1997, 106),         -- Phish
(7, 'Dave Matthews Band Magic Brownies', 2007, 108), -- Dave Matthews
(8, 'Half Baked', 2000, NULL),        -- No celebrity
(9, 'Chocolate Chip Cookie Dough', 1991, NULL), -- No celebrity
(10, 'Chunky Monkey', 1988, NULL),     -- No celebrity
(11, 'Chocolate Fudge Brownie', 1991, NULL), -- No celebrity
(12, 'Churray for Churros', 2021, NULL), -- Non-celebrity
(13, 'Mint Chocolate Cookie', 2001, NULL), -- Non-celebrity
(14, 'Peanut Butter Cup', 1989, NULL), -- Non-celebrity
(15, 'Coffee Toffee Bar Crunch', 1994, NULL), -- Non-celebrity
(16, 'Tiramisu', 2014, NULL);           -- Non-celebrity


INSERT INTO KrogerAvailability (KrogerID, IcecreamID, FullName, PintsInStock, LastMonthOrdered, NextMonthOrder)
VALUES 
(1, 1, 'Americone Dream', 100, 'September', 'November'),
(2, 2, 'Tonight Dough', 50, 'October', 'December'),
(3, 3, 'Cherry Garcia', 80, 'August', 'October'),
(4, 4, 'Imagine Whirled Peace', 70, 'September', 'November'),
(5, 5, 'Bob Marley’s One Love', 60, 'October', 'December'),
(6, 6, 'Phish Food', 120, 'September', 'November'),
(7, 7, 'Dave Matthews Band Magic Brownies', 50, 'August', 'November'),
(8, 8, 'Half Baked', 200, 'September', 'November'),
(9, 9, 'Chocolate Chip Cookie Dough', 150, 'October', 'December'),
(10, 10, 'Chunky Monkey', 130, 'September', 'November'),
(11, 11, 'Chocolate Fudge Brownie', 140, 'October', 'December'),
(12, 12, 'Churray for Churros', 100, 'September', 'November'),
(13, 13, 'Mint Chocolate Cookie', 90, 'October', 'December'),
(14, 14, 'Peanut Butter Cup', 60, 'August', 'October'),
(15, 15, 'Coffee Toffee Bar Crunch', 70, 'September', 'November'),
(16, 16, 'Tiramisu', 50, 'October', 'December');

-- select * from celebrities;
-- select * from icecreaminfo;
-- select * from krogeravailability;