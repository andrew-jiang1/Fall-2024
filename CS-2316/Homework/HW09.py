import pymysql
import getpass
from pprint import pprint
import csv
# No other imports allowed

'''
CS 2316 - Fall 2024 - HW09
 
First, run the provided dnd_weapons_armor.sql file to create the database. 
Yo cannot run this file until you have run the sql file
Download "battles.csv"
 
For the following functions,
  - use the cursor, to execute SQL statements
  - call connection.commit() to save changes you make to the database
  - to examine the different tables in the database, make use of the sql script provided!
 
Reference the pymysql handout for more details on using pymysql
HW09: This homework is due by Sunday, November 17th @ 11:59PM
'''

############################################################################
# THIS PART IS WRITTEN FOR YOU
############################################################################
def reset_database(cursor):
    ## weapon table queries
    
    d0 = "DROP table if exists battles;"
    d1 = "DROP TABLE IF EXISTS SimpleWeapons;"
    c1 = "CREATE TABLE SimpleWeapons (Name VARCHAR (100), Cost INT, Damage VARCHAR (1000), DamageType VARCHAR (1000), AverageDamage FLOAT, Weight FLOAT, Properties VARCHAR (1000), PRIMARY KEY (Name));"

    d2 = "DROP TABLE IF EXISTS MartialWeapons;"
    c2 = "CREATE TABLE MartialWeapons (Name VARCHAR (1000), Cost INT, Damage VARCHAR (1000), DamageType VARCHAR (1000), AverageDamage FLOAT, Weight FLOAT, Properties VARCHAR (1000));"

    ## armor table queries
    d3 = "DROP TABLE IF EXISTS LightArmor;"
    c3 = "CREATE TABLE LightArmor (Name VARCHAR (1000), ArmorClassAC VARCHAR (1000), Strength VARCHAR (1000), Stealth VARCHAR (1000), Weight DOUBLE, Cost INT);"
    
    d4 ="DROP TABLE IF EXISTS MediumArmor;"
    c4 = "CREATE TABLE MediumArmor (Name VARCHAR (1000), ArmorClassAC VARCHAR (1000), Strength VARCHAR (1000), Stealth VARCHAR (1000), Weight DOUBLE, Cost INT);"
    
    d5 = "DROP TABLE IF EXISTS HeavyArmor;"
    c5 = "CREATE TABLE HeavyArmor (Name VARCHAR (1000), ArmorClassAC VARCHAR (1000), Strength VARCHAR (1000), Stealth VARCHAR (1000), Weight DOUBLE, Cost INT);"

    cursor.execute(d0)
    cursor.execute(d1)
    cursor.execute(d2)
    cursor.execute(d3)
    cursor.execute(d4)
    cursor.execute(d5)

    cursor.execute(c1) # create the first three tables
    cursor.execute(c2)
    cursor.execute(c3)
    cursor.execute(c4)
    cursor.execute(c5)

############################################################################
# ANSWER THE QUESTIONS BELOW. USE THE CURSOR TO EXECUTE YOUR QUERIES
############################################################################


def light_armor_cost(cursor):
    '''
    QUERY 1

    Send a query to the dnd_weapons_armor database and return the name and cost for all items in the LightArmor table.


    ===== LightArmor Table =====
    (('Padded', 500),
    ('Leather', 1000),
    ('Studded Leather', 4500))

    '''
    query = "select Name, Cost from LightArmor;"
    
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def heavy_weapons(cursor):
    '''
    QUERY 2

    Send a query to the dnd_weapons_armor database and return all values from the SimpleWeapons table 
    where the weight is less than or equal to 2 and the property contains thrown.

    
    ============================= SimpleWeapons Table =============================
    (('Dagger', 200, '1d4', 'piercing', 3.0, 1.0, 'Finesse, light, thrown (20/60)'),
    ('Dart', 5, '1d4', 'piercing', 3.0, 0.25, 'Finesse, thrown (20/60)'),
    ('Handaxe', 500, '1d6', 'slashing', 4.0, 2.0, 'Light, thrown (20/60)'),
    ('Javelin', 50, '1d6', 'piercing', 4.0, 2.0, 'Thrown (30/120)'),
    ('Light hammer', 200, '1d4', 'bludgeoning', 3.0, 2.0, 'Light, thrown (20/60)'))

    '''
    query = "select * from SimpleWeapons where weight <= 2 and Properties like '%thrown%' ;"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def new_weapons(cursor, Name, ArmorClassAC, Strength, Stealth, Weight, Cost):
    '''
    QUERY 3

    Insert a new armor into the LightArmor table. All values are given as parameters. 

    =========== Updated LightArmor Table ===========
    ('Padded', '11 + Dex modifier', '-', 'Disadvantage', 8.0, 500)
    ('Leather', '11 + Dex modifier', '-', '-', 10.0, 1000)
    ('Studded Leather', '12 + Dex Modifier', '-', '-', 13.0, 4500)
    ('Shadow Cloak', '12 + Dex modifier', '-', 'Advantage', 5.0, 7000)
    
    '''
    query = "insert into LightArmor values (%s, %s, %s, %s,  %s, %s);"

    cursor.execute(query,(Name,ArmorClassAC,Strength,Stealth,Weight,Cost))
    result = cursor.fetchall()
    return result


def suit_up(cursor, armorList):
    '''
    QUERY 4

    You don't want to be seen wearing any basic armor, so it's time to add some fancy options to the HeavyArmor table. 
    Given a list of tuples of different armors, add this list into the HeavyArmor table. 
    
    YOU MUST DO THIS QUESTION WITHOUT THE USE OF LOOPS

    =========== Updated HeavyArmor Table ===========
    ('Ring Mail', '14', '-', 'Disadvantage', 40.0, 3000)
    ('Chain Mail', '16', 'Str 13', 'Disadvantage', 55.0, 7500)
    ('Splint', '17', 'Str 15', 'Disadvantage', 60.0, 20000)
    ('Plate', '18', 'Str 15', 'Disadvantage', 65.0, 150000)
    ('Diamond', '18', 'Str 16', 'Disadvantage', 60.0, 200000)
    ('Mithril', '19', 'Str 15', '-', 55.0, 500000)
    ('Adamantium', '17', 'Str 14', '-', 60.0, 200000)
    ('Beskar', '18', 'Str 15', 'Disadvantage', 65.0, 50000)
    '''
    new = armorList
    cursor.executemany("insert into HeavyArmor values (%s,%s,%s,%s,%s,%s);",new)
    result = cursor.fetchall()
    return result
    

def battling(cursor, infile):
    '''
    QUERY 5

    Make another table called battles using the csv called battles.csv provided and insert the data.
    
    Make sure that each attribute of the CSV meets the constraints of the table 
    (you can assume the Date will be in the correct format)

    You will have 5 attributes:
    - BattleName                - non null string of 50 characters at max as a PRIMARY KEY
    - Date                      - non null string of 25 characters at max
    - Location                  - non null string from the set {'Forest', 'Castle', 'Cliffs', 'Mountains'}
    - WeaponName                - string of 25 characters at max, FOREIGN KEY taken from the name of the SimpleWeapons Table
    - Winner                    - non null string of 25 characters at max
    - Casualties                - non null Integer

    Hint: You should use ENUM for the type attribute. Also, be careful with the quotations ...

    =========== Battles Table ===========
    ('Battle of the Wilderness', '1/15/2024', 'Forest', 'Club', 'Knights', 1000)
    ('Duel at Dawn', '4/5/2024', 'Cliffs', 'Dagger', 'Rogues', 420)
    ('Siege of the Castle', '2/20/2024', 'Castle', 'Quarterstaff', 'Wizards', 76)
    ('The Great Hunt', '5/12/2024', 'Mountains', 'Mace', 'Rangers', 4)

    '''
    battle = ("create table battles (BattleName varchar(50) NOT NULL, Date varchar(25) NOT NULL, Location enum('Forest', 'Castle', 'Cliffs', 'Mountains') NOT NULL,WeaponName varchar(25), Winner varchar(25) NOT NULL, Casualties INT NOT NULL, PRIMARY KEY (BattleName), FOREIGN KEY (WeaponName) REFERENCES SimpleWeapons(Name));")
    cursor.execute(battle)

    with open(infile, 'r') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            b = row[0]
            d = row[1]
            l = row[2]
            w = row[3]
            wi = row[4]
            c = row[5]

            if len(b) <= 50 and l in ['Forest', 'Castle', 'Cliffs', 'Mountains'] and c.isdigit():
                cursor.execute("select Name from SimpleWeapons where name = %s", w)
                if cursor.fetchone():  
                    query = "insert into battles values (%s,%s,%s,%s,%s,%s);"
                    cursor.execute(query, (b,d,l,w,wi,c))



    

def winning_wizards(cursor):
    '''
    QUERY 6

    Update your battles table so whereever the Wizards win, the weapon they win with is the Quarterstaff.
    Run this AFTER questions 5.

    =========== Updated Battles Table ===========
    ('Battle of the Wilderness', '1/15/2024', 'Forest', 'Club', 'Knights', 1000)
    ('Duel at Dawn', '4/5/2024', 'Cliffs', 'Dagger', 'Rogues', 420)
    ('Siege of the Castle', '2/20/2024', 'Castle', 'Quarterstaff', 'Wizards', 76)
    ('The Great Hunt', '5/12/2024', 'Mountains', 'Mace', 'Rangers', 4)

    '''
    query = "update battles set WeaponName = 'Quarterstaff' where Winner like '%Wizards%'"
    result = cursor.execute(query)
    return result
  
def no_club_for_you(cursor):
    '''
    QUERY 7

    Delete the Club from the SimpleWeapons table and delete other rows that may refer to the primary key of Club.
    Run this AFTER questions 5 and 6.


    =========== Updated Battles Table ===========
    ('Duel at Dawn', '4/5/2024', 'Cliffs', 'Dagger', 'Rogues', 420)
    ('Siege of the Castle', '2/20/2024', 'Castle', 'Quarterstaff', 'Wizards', 76)
    ('The Great Hunt', '5/12/2024', 'Mountains', 'Mace', 'Rangers', 4)
    
    =========== Updated SimpleWeapons Table ===========
    ('Crossbow, light', 2500, '1d8', 'piercing', 5.0, 5.0, 'Ammunition, range (80/320), loading, two-handed')
    ('Dagger', 200, '1d4', 'piercing', 3.0, 1.0, 'Finesse, light, thrown (20/60)')
    ('Dart', 5, '1d4', 'piercing', 3.0, 0.25, 'Finesse, thrown (20/60)')
    ('Greatclub', 20, '1d8', 'bludgeoning', 5.0, 10.0, 'Two-handed')
    ('Handaxe', 500, '1d6', 'slashing', 4.0, 2.0, 'Light, thrown (20/60)')
    ('Javelin', 50, '1d6', 'piercing', 4.0, 2.0, 'Thrown (30/120)')
    ('Light hammer', 200, '1d4', 'bludgeoning', 3.0, 2.0, 'Light, thrown (20/60)')
    ('Mace', 500, '1d6', 'bludgeoning', 4.0, 4.0, 'None')
    ('Quarterstaff', 20, '1d6', 'bludgeoning', 4.0, 4.0, 'Versatile (1d8)')
    ('Shortbow', 2500, '1d6', 'piercing', 4.0, 2.0, 'Ammunition, range (80/320), two-handed')
    ('Sickle', 100, '1d4', 'slashing', 3.0, 2.0, 'Light')
    ('Sling', 10, '1d4', 'bludgeoning', 3.0, 0.0, 'Ammunition, range (30/120)')
    ('Spear', 100, '1d6', 'piercing', 4.0, 3.0, 'Thrown (20/60), versatile (1d8)')  

    '''
    battle = "delete from battles where WeaponName like 'Club%'"
    cursor.execute(battle)
    club = "delete from SimpleWeapons where Name like 'Club%'"
    cursor.execute(club)


############################################################################
# TESTING PORTION
############################################################################
def populate_database(cursor):
    

    #populate simple weapons
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Club', 10, '1d4', 'bludgeoning', 3, 2.0, 'Light');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Dagger', 200, '1d4', 'piercing', 3, 1.0, 'Finesse, light, thrown (20/60)');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Greatclub', 20, '1d8', 'bludgeoning', 5, 10.0, 'Two-handed');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Handaxe', 500, '1d6', 'slashing', 4, 2.0, 'Light, thrown (20/60)');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Javelin', 50, '1d6', 'piercing', 4, 2.0, 'Thrown (30/120)');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Light hammer', 200, '1d4', 'bludgeoning', 3, 2.0, 'Light, thrown (20/60)');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Mace', 500, '1d6', 'bludgeoning', 4, 4.0, 'None');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Quarterstaff', 20, '1d6', 'bludgeoning', 4, 4.0, 'Versatile (1d8)');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Sickle', 100, '1d4', 'slashing', 3, 2.0, 'Light');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Spear', 100, '1d6', 'piercing', 4, 3.0, 'Thrown (20/60), versatile (1d8)');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Crossbow, light', 2500, '1d8', 'piercing', 5, 5.0, 'Ammunition, range (80/320), loading, two-handed');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Dart', 5, '1d4', 'piercing', 3, 0.25, 'Finesse, thrown (20/60)');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Shortbow', 2500, '1d6', 'piercing', 4, 2.0, 'Ammunition, range (80/320), two-handed');")
    cursor.execute("INSERT INTO SimpleWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Sling', 10, '1d4', 'bludgeoning', 3, 0.0, 'Ammunition, range (30/120)');")

    #populate amrtial weapons
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Battleaxe', 1000, '1d8', 'slashing', 5.0, 4.0, 'Versatile (1d10)');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Flail', 1000, '1d8', 'bludgeoning', 5.0, 2.0, 'None');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Glaive', 2000, '1d10', 'slashing', 6.0, 6.0, 'Heavy, reach, two-handed');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Greataxe', 3000, '1d12', 'slashing', 7.0, 7.0, 'Heavy, two-handed');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Greatsword', 5000, '2d6', 'slashing', 8.0, 6.0, 'Heavy, two-handed');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Halberd', 2000, '1d10', 'slashing', 6.0, 6.0, 'Heavy, reach, two-handed');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Lance', 1000, '1d12', 'piercing', 7.0, 6.0, 'Reach, special');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Longsword', 1500, '1d8', 'slashing', 5.0, 3.0, 'Versatile (1d10)');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Maul', 1000, '2d6', 'bludgeoning', 8.0, 10.0, 'Heavy, two-handed');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Morningstar', 1500, '1d8', 'piercing', 5.0, 4.0, 'None');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Pike', 500, '1d10', 'piercing', 6.0, 18.0, 'Heavy, reach, two-handed');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Rapier', 2500, '1d8', 'piercing', 5.0, 2.0, 'Finesse');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Scimitar', 2500, '1d6', 'slashing', 4.0, 3.0, 'Finesse, light');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Shortsword', 1000, '1d6', 'piercing', 4.0, 2.0, 'Finesse, light');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Trident', 500, '1d6', 'piercing', 4.0, 4.0, 'Thrown (20/60), versatile (1d8)');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('War pick', 500, '1d8', 'piercing', 5.0, 2.0, 'None');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Warhammer', 1500, '1d8', 'bludgeoning', 5.0, 2.0, 'Versatile (1d10)');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Whip', 200, '1d4', 'slashing', 3.0, 3.0, 'Finesse, reach');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Blowgun', 1000, '1', 'piercing', 0.0, 1.0, 'Ammunition, range (25/100), loading');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Crossbow, hand', 7500, '1d6', 'piercing', 4.0, 3.0, 'Ammunition, range (30/120), light, loading');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Crossbow, heavy', 5000, '1d10', 'piercing', 6.0, 18.0, 'Ammunition, range (100/400), heavy, loading, two-handed');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Longbow', 5000, '1d8', 'piercing', 5.0, 2.0, 'Ammunition, range (150/600), heavy, two-Handed');")
    cursor.execute("INSERT INTO MartialWeapons(Name, Cost, Damage, DamageType, AverageDamage, Weight, Properties) VALUES ('Net', 100, '0', 'None', 0.0, 3.0, 'Special, thrown (5/15)');")
    
    #populate light armor
    cursor.execute("INSERT INTO LightArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Padded', '11 + Dex modifier', '-', 'Disadvantage', 8.0, 500);")
    cursor.execute("INSERT INTO LightArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Leather', '11 + Dex modifier', '-', '-', 10.0, 1000);")
    cursor.execute("INSERT INTO LightArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Studded Leather', '12 + Dex Modifier', '-', '-', 13.0, 4500);")
    
    #populate medium armor
    cursor.execute("INSERT INTO MediumArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Hide', '12 + Dex modifier (max 2)', '-', '-', 12.0, 1000);")
    cursor.execute("INSERT INTO MediumArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Chain Shirt', '13 + Dex modifier (max 2)', '-', '-', 20.0, 5000);")
    cursor.execute("INSERT INTO MediumArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Scale Mail', '14 + Dex modifier (max 2)', '-', 'Disadvantage', 45.0, 5000);")
    cursor.execute("INSERT INTO MediumArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Spiked Armor', '14 + Dex modifier (max 2)', '-', 'Disadvantage', 45.0, 7500);")
    cursor.execute("INSERT INTO MediumArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Breastplate', '14 + Dex modifier (max 2)', '-', '-', 20.0, 40000);")
    cursor.execute("INSERT INTO MediumArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Halfplate', '15 + Dex modifier (max 2)', '-', 'Disadvantage', 40.0, 75000);")
    
    #popluate heavy armor
    cursor.execute("INSERT INTO HeavyArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Ring Mail', '14', '-', 'Disadvantage', 40.0, 3000);")
    cursor.execute("INSERT INTO HeavyArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Chain Mail', '16', 'Str 13', 'Disadvantage', 55.0, 7500);")
    cursor.execute("INSERT INTO HeavyArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Splint', '17', 'Str 15', 'Disadvantage', 60.0, 20000);")
    cursor.execute("INSERT INTO HeavyArmor(Name, ArmorClassAC, Strength, Stealth, Weight, Cost) VALUES ('Plate', '18', 'Str 15', 'Disadvantage', 65.0, 150000);")




def main():
    user_password = getpass.getpass('\n# Enter your MySQL Server password: ')

    connection = pymysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = user_password,
                                 db = 'dnd_weapons_armor',
                                 charset = "utf8mb4",
                                 cursorclass = pymysql.cursors.Cursor)

    # Always create the cursor
    cursor = connection.cursor()

    reset_database(cursor)
    populate_database(cursor)


    ############################################################################
    # TEST CASES BELOW.
    ############################################################################
    # WE RECOMMEND YOU RUN EACH OF THEM SEPARATELY for 1-4
    # WE RECOMMEND YOU RUN THESE TOGETHER for 5-7  (overthwise your code may error)
    ############################################################################
    ############################################################################

    # QUESTION 1 TEST CASE
    print('Question 1')
    pprint(light_armor_cost(cursor))

    # QUESTION 2 TEST CASE
    print('Question 2')
    pprint(heavy_weapons(cursor))

    # QUESTION 3 TEST CASE
    print('Question 3')
    new_weapons(cursor, "Shadow Cloak", "12 + Dex modifier", "-", "Advantage", 5.0, 7000)
    print('=========== Updated LightArmor Table ===========')
    cursor.execute("SELECT * FROM LightArmor;")
    for row in cursor.fetchall():
        print(row)

    # QUESTION 4 TEST CASE
    print('Question 4')
    armorList = [('Diamond', 18, 'Str 16', 'Disadvantage', 60, 200000),('Mithril', 19, 'Str 15', '-', 55, 500000), ('Adamantium', 17, 'Str 14', '-', 60, 200000), ('Beskar', 18, 'Str 15', 'Disadvantage', 65, 50000)]
    suit_up(cursor, armorList)
    print('=========== Updated HeavyArmor Table ===========')
    cursor.execute("SELECT * FROM HeavyArmor;")
    for row in cursor.fetchall():
        print(row)


    # QUESTION 5 TEST CASE
    print('Question 5')
    battling(cursor, 'battles.csv')
    print('=========== Battles Table ===========')
    cursor.execute("SELECT * FROM battles")  
    for row in cursor.fetchall():
        print(row)


    # QUESTION 6 TEST CASE
    print('Question 6')
    winning_wizards(cursor)
    print('=========== Battles Table ===========')
    cursor.execute("SELECT * FROM battles")  
    results = cursor.fetchall()
    for row in results:
        print(row)


    # QUESTION 7 TEST CASE
    print('Question 7')
    no_club_for_you(cursor)
    print('=========== Updated Battles Table ===========')
    cursor.execute("SELECT * FROM battles")  
    results = cursor.fetchall()
    for row in results:
        print(row)
    print('=========== Updated SimpleWeapons Table ===========')
    cursor.execute("SELECT * FROM SimpleWeapons")  
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Always commit the connection when you are done
    connection.commit()


if __name__ == "__main__":
    main()
