import pymysql
from pprint import pprint
import getpass

## NOTES:

# CS 2316 - Fall 2024 - HW08 MySQL
# HW08: This homework is due by Sunday, November 3rd @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype if a return is required
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW08.py - Your submission should be named exactly HW08.py
#   - Print your variables as you code in order to see what values they have
#   - Please make sure that the capitalization of your table and column names matches the
#     capitalization in the database.

def create_cursor(host_name, user_name, pw, db_name):
    try:
        connection = pymysql.connect(host = host_name, user = user_name, password = pw, db = db_name, \
                                    charset = "utf8mb4", cursorclass = pymysql.cursors.Cursor)
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        print(e)
        print(f"Couldn't log in to MySQL server using this password: {pw}.\n")

def old_flavors(cursor):
    '''
    QUERY 1

    Create a query that will return the name of all the ice cream flavors that were created before the year 2000.

    Expected Output:
    (('Cherry Garcia',),
     ('Phish Food',),
     ('Chocolate Chip Cookie Dough',),
     ('Chunky Monkey',),
     ('Chocolate Fudge Brownie',),
     ('Peanut Butter Cup',),
     ('Coffee Toffee Bar Crunch',))
    '''
    query = "select FullName from IceCreamInfo where YearCreated < 2000;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def party(cursor):
    '''
    QUERY 2

    You love ice cream, specifically Ben and Jerry's ice cream, and want to buy lots of it for your birthday party.

    Create a query that returns the 'FullName' and 'PintsInStock' of Ben and Jerry's ice creams at Kroger that have more than 100 pints in stock
    OR Have less than 75 pints in stock but are going to be ordered in October (this is referring to the NextMonthOrder column). Sort the results alphabetically by flavor name.

    Now your party will be awesome.

    Expected Output:
    (('Chocolate Chip Cookie Dough', 150)
    ('Chocolate Fudge Brownie', 140)
    ('Chunky Monkey',   130)
    ('Half Baked',  200)
    ('Peanut Butter Cup',   60)
    ('Phish Food',  120))

    '''
    query = "select FullName,PintsInStock from KrogerAvailability where PintsInStock > 100 or (PintsInStock < 75 and NextMonthOrder = 'October') order by FullName ASC;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def trying_flavors(cursor):
    '''
    QUERY 3

    You are unfamiliar with Ben and Jerry's flavors, but you want to try a few flavors that are in abundance at Kroger. 
    However, you don't want to be basic, so you don't want to get the one that's in the highest stock. Return the 
    names of the three flavors with the most pints in stock, not including the flavor with the most pints in stock. 

    Expected Output:
       (('Chocolate Chip Cookie Dough',), ('Chocolate Fudge Brownie',), ('Chunky Monkey',))

    '''
    query = "select FullName from KrogerAvailability order by PintsInStock desc Limit 3 Offset 1;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def more_than_200(cursor):
    '''
    QUERY 4

    You are interested in understanding the number of different ice cream flavors ordered in each month.
    Write a query that returns the LastMonthOrdered and the count of distinct ice cream flavors (FullName) from the KrogerAvailability table,
    but only for months where the total number of pints available (PintsInStock) exceeds 200. Sort your results in descending order
    by LastMonthOrdered.

    Expected Output:
    (('September',   7)
    ('October', 6))
    '''

    query = "select LastMonthOrdered, count(distinct(FullName)) from KrogerAvailability group by LastMonthOrdered having sum(PintsInStock) > 200 order by LastMonthOrdered Desc;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def order_quantities(cursor):
    '''
    QUERY 5

    You are a Kroger employee who wants to see how many flavors were ordered in recent months. However,
    you also do not want to include months that have future orders scheduled. Return the list of the last months when flavors
    were ordered and the number of flavors ordered, and sort alphabetically by month.

    Expected Output:
    (('August', 3), ('September', 7))
    '''

    query = "select LastMonthOrdered, count(distinct(FullName)) from KrogerAvailability where LastMonthOrdered not in (select distinct(NextMonthOrder) from KrogerAvailability) group by LastMonthOrdered order by LastMonthOrdered ASC;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def october_or_21st_century(cursor):
    '''
    QUERY 6

    Write a query that retrieves the average number of pints in stock for each NextMonthOrder from the IceCreamInfo and KrogerAvailability tables.
    The query should include only ice cream flavors created in or after the year 2000, or those with a NextMonthOrder set to 'October'.
    Ensure the results are grouped by NextMonthOrder.

    Expected Output:
    ((November,    104.0000)
    (December,    62.5000)
    (October, 70.0000))
    '''
    
    query = "select NextMonthOrder, avg(PintsInStock) from IceCreamInfo i natural join KrogerAvailability k where (YearCreated >= 2000 or NextMonthOrder = 'October') group by k.NextMonthOrder;"
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def collabs_and_recents(cursor):
    '''
    QUERY 7

    You really like to listen to music while you eat ice cream. You also want to try some of the newer flavors. Return all of the 
    names of flavors and the year they were created for all flavors that are collaborations with musicians or all flavors 
    created after 2015.

    Expected Output:
    (('Cherry Garcia', 1987),
    ('Imagine Whirled Peace', 2008),
    ('Bob Marley’s One Love', 2016),
    ('Dave Matthews Band Magic Brownies', 2007),
    ('Churray for Churros', 2021))
    '''

    query = "select FullName, YearCreated from IceCreamInfo left join Celebrities on CelebID = CelebrityID where Occupation = 'Musician' or YearCreated > 2015;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def musicless_months(cursor):
    '''
    QUERY 8

    Create a query that will return the month and the average pints in stock (as an integer) in descending order for all ice creams
    not sponsored by a musician, grouped by the last month an order was placed. Round the averages to be whole numbers, and sort 
    your results by this rounded average.

    Expected Output:
    (('August', Decimal('60')),
     ('October', Decimal('96')),
     ('September', Decimal('120')))
    '''
    
    query = "select LastMonthOrdered, round(avg(PintsInStock)) from IceCreamInfo i left join Celebrities c on i.CelebrityID = c.CelebID natural join KrogerAvailability k where c.Occupation not like 'Musician%' or i.CelebrityID is null group by LastMonthOrdered order by round(avg(PintsInStock));"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def main():

    ######################## Insert MySQL Server password if applicable ########################

    user_password = getpass.getpass('\n# Enter your MySQL Server password: ')
    cursor = create_cursor('localhost', 'root', user_password, 'BenAndJerrys')

    # If you do not want to enter your password every time, you can replace
    # user_password with your password (as a string) and comment out
    # this line of code: user_password = getpass.getpass('\n# Enter your MySQL Server password: ')
    # We recommend resetting this before uploading your HW.

    ########################### Test Cases ###########################

    # Query 1
    print(">>> q1(cursor)")
    pprint(old_flavors(cursor))

    # # Query 2
    print(">>> q2(cursor)")
    pprint(party(cursor))

    # # Query 3
    print(">>> q3(cursor)")
    pprint(trying_flavors(cursor))

    # # Query 4
    print(">>> q4(cursor)")
    pprint(more_than_200(cursor))

    # # Query 5
    print(">>> q5(cursor)")
    pprint(order_quantities(cursor))

    # # Query 6
    print(">>> q6(cursor)")
    pprint(october_or_21st_century(cursor))

    # # Query 7
    print(">>> q7(cursor)")
    pprint(collabs_and_recents(cursor))

    # # Query 8
    print(">>> q8(cursor)")
    pprint(musicless_months(cursor))


if __name__ == '__main__':
    main()
