# CS 2316 - Fall 2024 - HW05
# HW05: This homework is due by October 16th @ 11:59PM through Gradescope

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW05.py  - Your submission should be named exactly HW05.py
#   - We will NOT help with Q1, it should have been completed in HW02

## CODE CARBON LEADERBOARD:
#This homework as EXTRA CREDIT associated with it. In order to be eligible, you must pass all of the autograder test cases (have a 10/10)
#This assingnement has a leaderboard for carbon emissions efficiency, and the top 10% of students will get 3 bonus points
#That is the top 10% witht he lowest carbon emissions. Note you can submit multiple times in an effort to write more efficient code
#You will be able to put your leaderboard submission under any name, Vulgar names will result in a 0/10 for this assignment


from pprint import pprint
import csv
import numpy as np 
import pandas as pd 

def unfriendly_data_cleaner(input_file):
    """
    QUESTION 01

    IMPORTANT - This is the same question from homework 2 question 4, please COPY AND PASTE your answer so you can compare
    with question 7 (and so you can compete in the time trial)
    
    This should only include methods learned by the time of questions 2 (manual list manipulation, File I/O...)

    You have been given a csv file with information about the 2023 F1 season! Complete data! So exciting! 
    The person who made the data messed up, and it's kind of hard to work with. Since you're such a nice
    person, you volunteered to help them clean up the data. Here's everything that they want you to do:
    
    1. There are two identical driver columns and two idential team columns, drop one of each
    2. Replace all empty values in Q1, Q2, and Q3 as 'N/A'
    3. Drop all rows that contain DNF or DNS in Q1, Q2, and Q3
    4. Rename Q1, Q2, and Q3 to 'Qualifying 1', 'Qualifying 2', and 'Qualifying 3'
    5. Split the driver's names into two columns. Rename the original 'Driver' column into 'Driver First Name' and 
        'Driver Last Name' at the same index.
    6. Replace occurence of 'Alfa Romeo Ferrari' with 'Kick Sauber Ferrari'
    7. Create a new column called "Engine Manufacturer" right after the team name column populated with the
        last word of each team name. If the team name is only one word, duplicate it.
    
    Write the data out to a csv file called 'clean_2023season_stats.csv’ and return the list of lists
    
    Hint: use .insert()
    Hint 2: do these steps in order

    Args:
        input_file (2023season_race_stats.csv)
    Returns:
        list of lists

    >>> pprint(friendly_data_cleaner('2023season_race_stats.csv'))
    [['Track', 'Position', 'No', 'Driver First Name', 'Driver Last Name', 'Team', 'Engine Manufacturer',
        'Qualifying 1', 'Qualifying 2', 'Qualifying 3', 'Average Qualifying Time', 'Laps', 'Starting Grid',
        'Laps', 'Time/Retired', 'Points', 'Set Fastest Lap', 'Fastest Lap Time'],
     ['Bahrain', '1', '1', 'Max', 'Verstappen', 'Red Bull Racing Honda RBPT', 'RBPT', '01:31.3', '01:30.5',
        '01:29.7', '01:30.5', '15', '1', '57', '33:56.7', '25', 'No', '01:36.2'],
     ['Bahrain', '2', '11', 'Sergio', 'Perez', 'Red Bull Racing Honda RBPT', 'RBPT', '01:31.5', '01:30.7',
        '01:29.8', '01:30.7', '15', '2', '57', '11.987', '18', 'No', '01:36.3'],
     ...
     ['Abu Dhabi', '20', '20', 'Kevin', 'Magnussen', 'Haas Ferrari', 'Ferrari', '01:24.8', 'N/A', 'N/A',
        '01:24.8', '6', '17', '57', '+1 lap', '0', 'No', '01:29.9']]
    """
    
    with open("2023season_race_stats.csv") as f:
        reader = csv.reader(f)
        lt = list(reader)
        h = lt[0]
        r = lt[1:]

        nh = []
        rdup =[]    

        for count, col in enumerate(h):
            if col[-4:] != "_Dup":
                nh.append(col)
            else:
                rdup.append(count)
        
        nrs = []
        for row in r:
            nr = [add for x,add in enumerate(row) if x not in rdup]
            nrs.append(nr)

        q1 = nh.index("Q1")
        q2 = nh.index("Q2")
        q3 = nh.index("Q3")

        for row in nrs:
            row[q1] = row[q1] if row[q1] else "N/A"
            row[q2] = row[q2] if row[q2] else "N/A"
            row[q3] = row[q3] if row[q3] else "N/A"
        
        cr = []
        for row in nrs:
            if "DNF" not in [row[q1],row[q2],row[q3]] and "DNS" not in [row[q1],row[q2],row[q3]]:
                cr.append(row)

        nh[q1] = "Qualifying 1"
        nh[q2] = "Qualifying 2"
        nh[q3] = "Qualifying 3"    

        driver_name = nh.index("Driver")
        nh[driver_name] = "Driver First Name"
        nh.insert(driver_name+1,"Driver Last Name")

        for row in cr:
            fname = row[driver_name].split(" ",1)
            row[driver_name] = fname[0]
            row.insert(driver_name + 1 , fname[1])

        tpos = nh.index("Team")
        for row in cr:
            if row[tpos] == "Alfa Romeo Ferrari":
                row[tpos] = "Kick Sauber Ferrari"
        
        nh.insert(tpos+1, "Engine Manufacturer")
        for row in cr:
            tname = row[tpos]
            engine = tname.split()[-1] if len(tname.split()) > 1 else tname
            row.insert(tpos+1, engine)
        
        with open("clean_2023season_stats.csv","w") as f:
            writer = csv.writer(f)
            writer.writerow(nh)
            writer.writerows(cr)

    return [nh] + cr    


def pandas_data_cleaner(input_file):
    """
    QUESTION 02

    IMPORTANT - This is the same question as above, BUT NOW, perform the same cleaning as you did above,
    but using Pandas methods you have learned!! (there is one difference in the name you write the file to)

    You have been given a csv file with information about the 2023 F1 season! Complete data! So exciting! 
    The person who made the data messed up, and it's kind of hard to work with. Since you're such a nice
    person, you volunteered to help them clean up the data. Here's everything that they want you to do:
    
    1. There are two identical driver columns and two idential team columns, drop one of each
    2. Replace all empty values in Q1, Q2, and Q3 as 'N/A'
    3. Drop all rows that contain DNF or DNS in Q1, Q2, and Q3
    4. Rename Q1, Q2, and Q3 to 'Qualifying 1', 'Qualifying 2', and 'Qualifying 3'
    5. Split the driver's names into two columns. Rename the original 'Driver' column into 'Driver First Name' and 
        'Driver Last Name' at the same index.
    6. Replace occurence of 'Alfa Romeo Ferrari' with 'Kick Sauber Ferrari'
    7. Create a new column called "Engine Manufacturer" right after the team name column populated with the
        last word of each team name. If the team name is only one word, duplicate it.
    8. (NEW) Make sure you reset your index and have no extra columns, aka drop the new index column (You may also need to make sure types are consistent 
        between question 1 and this question)
    9. (NEW) When you read in your CSV file using pandas, your last column (Fastest Lap Time) will default the empty strings with NaN
        Esnure you change these back to empty strings

    Write the data out to a csv file called 'pandas_2023season_stats.csv’ and return the pandas dataframe

    NOTE: This should perfectly match your output of Question 1

    Args:
        input_file (2023season_race_stats.csv)
    Returns:
        pandas DataFrame

    >>> pprint(friendly_data_cleaner('2023season_race_stats.csv'))
        Track Position  No Driver First Name  ... Time/Retired Points Set Fastest Lap Fastest Lap Time
    0      Bahrain        1   1               Max  ...      33:56.7     25              No          01:36.2
    1      Bahrain        2  11            Sergio  ...       11.987     18              No          01:36.3
    2      Bahrain        3  14          Fernando  ...       38.637     15              No          01:36.2
    3      Bahrain        4  55            Carlos  ...       48.052     12              No          01:37.1
    4      Bahrain        5  44             Lewis  ...       50.977     10              No          01:36.5
    ..         ...      ...  ..               ...  ...          ...    ...             ...              ...
    422  Abu Dhabi       15  27              Nico  ...       83.696      0              No          01:29.2
    423  Abu Dhabi       17  24            Guanyu  ...       89.422      0              No          01:28.7
    424  Abu Dhabi       18  55            Carlos  ...          DNF      0              No          01:29.5
    425  Abu Dhabi       19  77          Valtteri  ...       +1 lap      0              No          01:29.9
    426  Abu Dhabi       20  20             Kevin  ...       +1 lap      0              No          01:29.9

    [427 rows x 16 columns]
    """
    
    cdf = pd.read_csv("2023season_race_stats.csv")
    
    cdf1 = cdf.drop(["Driver_Dup","Team_Dup"],axis = 1)

    cdf1[["Q1","Q2","Q3"]] = cdf1[["Q1","Q2","Q3"]].fillna("N/A")

    cdf1 = cdf1[(cdf1["Q1"] != "DNF") & (cdf1["Q1"] != "DNS")]
    cdf1 = cdf1[(cdf1["Q2"] != "DNF") & (cdf1["Q2"] != "DNS")]
    cdf1 = cdf1[(cdf1["Q3"] != "DNF") & (cdf1["Q3"] != "DNS")]

    cdf1.rename(columns = {"Q1" : "Qualifying 1"},inplace=True)
    cdf1.rename(columns = {"Q2" : "Qualifying 2"},inplace=True)
    cdf1.rename(columns = {"Q3" : "Qualifying 3"},inplace=True)

    cdf1[["Driver First Name", "Driver Last Name"]] = cdf1["Driver"].str.split(" ", n = 1, expand = True)
    cdf1 = cdf1.drop(["Driver"],axis = 1)

    cdf1["Team"] = cdf1["Team"].replace("Alfa Romeo Ferrari","Kick Sauber Ferrari")

    cdf1["Engine Manufacturer"] = cdf1["Team"].str.split().str[-1]

    cdf1[["No","Laps","Starting Grid","Points"]] = cdf1[["No","Laps","Starting Grid","Points"]].astype(str)

    cdf1[["Fastest Lap Time"]] = cdf1[["Fastest Lap Time"]].fillna("")

    cdf1 = cdf1.reset_index(drop = True)

    cdf2 = cdf1.iloc[:,[0,1,2,13,14,3,15,4,5,6,7,8,9,10,11,12]]

    cdf2.to_csv("pandas_2023season_stats.csv",index=False)

    return cdf2



def place_finder(df, manufacturer):
    """
    QUESTION 03

    Given an engine manufacturer, calculate the average position of every racer with that manufacturer.
    You should not include positions for racers who were disqualified or did not compete.
    Round your answer to two digits. 
    
    Args:
        Pandas DataFrame
    Returns:
        float 

    >>> print(place_finder(data, "Ferrari"))

    11.37

    """
    
    vdf = pd.read_csv("pandas_2023season_stats.csv")

    vdf1 = vdf[vdf["Engine Manufacturer"] == manufacturer]

    vdf1 = vdf1[(vdf1["Position"] != "NC") & (vdf1["Position"] != "DQ")]

    vdf1 = vdf1["Position"].astype(int).mean().round(2)

    return vdf1



def left_behind(df):
    """
    QUESTION 04

    Return a DataFrame containing the number of laps each driver is behind, 
    sorted by the number of laps in descending order. Only include drivers that have been lapped.
    The first column should be the Driver's full name, and the second is the number of laps each driver is behind. 
    Then rename the first column to be "Driver Full Name"

    Hint: .cat() may be a useful string method for this question

    Args:
        Pandas DataFrame
    Returns:
        Pandas DataFrame

    >>> print(left_behind(data))

            Driver Full Name Time/Retired
    111  Nico Hulkenberg      +2 laps
    14      Lando Norris      +2 laps
    110     Sergio Perez      +2 laps
    109     Yuki Tsunoda      +2 laps
    112   Logan Sargeant      +2 laps
    ..               ...          ...
    151    Nyck De Vries       +1 lap
    165      Guanyu Zhou       +1 lap
    166   Logan Sargeant       +1 lap
    11   Kevin Magnussen       +1 lap
    426  Kevin Magnussen       +1 lap


    """
    
    bdf = pd.read_csv("pandas_2023season_stats.csv")

    bdf1 = bdf[(bdf["Time/Retired"] == "+1 lap") | (bdf["Time/Retired"] == "+2 laps")]

    bdf1["Driver Full Name"] = bdf1["Driver First Name"] + " " + bdf1["Driver Last Name"]

    bdf1 = bdf1[["Driver Full Name","Time/Retired"]]

    bdf1 = bdf1.sort_values(by = "Time/Retired", ascending = False, inplace = False)

    return bdf1

def stat_summary(df):
    """
    QUESTION 05 

    Using our cleaned sheet, we want to get some results grouped by each team's performace in each track.
    After taking out the racers that were disqualified or did not compete (DQ or NC), 
    please calculate the average position (renamed to AveragePosition) and total points (renamed to TotalTeamPoints) 
    for each team on each track.

    Then sort it by track and mean position (BEWARE...make sure to reset index before sorting).

    Args:
        Pandas Dataframe
    Return:
        Pandas Dataframe

    >>> print(stat_summary(friendly_data_cleaner('clean_2023season_stats.csv')))
                 Track                          Team  AveragePosition TotalTeamPoints
    8        Abu Dhabi    Red Bull Racing Honda RBPT              2.5            2612
    6        Abu Dhabi              McLaren Mercedes              5.5             108
    7        Abu Dhabi                      Mercedes              6.0             152
    2        Abu Dhabi  Aston Martin Aramco Mercedes              8.5              61
    0        Abu Dhabi         AlphaTauri Honda RBPT              9.5              40
    ..             ...                           ...              ...             ...
    208  United States  Aston Martin Aramco Mercedes              7.0               6
    215  United States             Williams Mercedes              9.5              21
    206  United States         AlphaTauri Honda RBPT             11.5              50
    210  United States                  Haas Ferrari             12.5              00
    211  United States           Kick Sauber Ferrari             12.5              00

        [216 rows x 4 columns]


    """
    
    fdf = pd.read_csv("pandas_2023season_stats.csv")

    fdf1 = fdf[(fdf["Position"] != "NC") & (fdf["Position"] != "DQ")]

    fdf1["Position"] = fdf1["Position"].astype(int)
    
    fdf1["Points"] = fdf1["Points"].astype(str)

    fdf1 = fdf1.groupby(["Track","Team"]).aggregate({"Position":"mean","Points":"sum"})

    fdf1 = fdf1.rename(columns = {"Position":"AveragePosition","Points":"TotalTeamPoints"})

    fdf1 = fdf1.reset_index()
    
    fdf1 = fdf1.sort_values(by = ["Track","AveragePosition"], ascending = True, inplace = False)

    return fdf1





def converted_laps(df):
    """
    QUESTION 06

    Using our result from question 2 as an input dataframe, we want to isolate our Fastest Lap Column.
    Return fastest lap times converted into seconds as a series making sure to only use the columns that have values (xx:xx.x)

    Hint: Use .apply() with a lambda function to change all the values in your column to what you want

    Args:
        Pandas Dataframe
    Returns:
        Pandas Series

    print(converted_laps(friendly_data_cleaner('clean_2023season_stats.csv')))
    >>> 0      96.2
        1      96.3
        2      96.2
        3      97.1
        4      96.5
               ...
        422    89.2
        423    88.7
        424    89.5
        425    89.9
        426    89.9
        Name: Fastest Lap Time, Length: 415, dtype: float64

    """
     # Use .apply() and .split()

    mdf = pd.read_csv("pandas_2023season_stats.csv")

    mdf1 = mdf["Fastest Lap Time"]

    mdf1 = mdf1.dropna()

    mdf1 = mdf1.astype(str)

    mdf1 = mdf1.str.split(":")

    def time_converter(minute,second):
        m = minute
        s = second
        time = (float(m) * 60) + float(s)
        return time
    
    mdf1 = mdf1.apply(lambda x: time_converter(x[0],x[1]))


    return mdf1


def TrackPerformance(df):
    '''
    QUESTION 07
    You are analyzing the performance data of racing teams for the 2023 season, and your goal is to investigate team performances by track, 
    filter high-performing teams, and analyze engine manufacturers based on their teams' performance.
 
    Using your pandas DataFrame from Question 2, filter out races where the position is marked as 'Not Complete'
    Group the data by 'Team' and 'Track', and calculate the total number of points earned by the team on that track.

    Using this newly created DataFrame, filter out the teams that scored more than 15 total points on any specific track.
    Go back to the original DataFrame and apply an additional filter to include only the teams that were found to have scored more than 15 points in total.
    Now, calculate the average points earned by each engine manufacturer, and sort the results from highest to lowest.
    Lastly, convert this Pandas DataFrame to JSON format named mean_points_by_engine.json and return the Pandas DataFrame.
    Yay! You're done! :)

    Args:
        Pandas Dataframe
    Returns:
        Pandas Series
 
    >>> print(TrackPerformance('input_file'))
        Engine Manufacturer
    RBPT        18.825000
    Ferrari      9.486486
    Mercedes     7.747826
    Renault      3.027778
    Name: Points, dtype: float64
    '''
    
    adf = pd.read_csv("pandas_2023season_stats.csv")

    adf1 = adf[adf["Position"] != "NC"]

    adf1 = adf1.groupby(["Team","Track"]).agg({"Points":"sum"})
    adf1 = adf1.reset_index()
    adf1 = adf1[adf1["Points"] > 15]["Team"].drop_duplicates()
    adf1 = adf1.astype(str)
    adf = adf[adf["Position"] != "NC"]
    adf2 = adf[adf["Team"].isin(adf1)]

    adf2 = adf2.groupby("Engine Manufacturer").agg({"Points":"mean"}).sort_values(by = "Points",ascending = False)

    adf2.to_json("mean_points_by_engine.json")

    return adf2


if __name__ == "__main__":
    print("Question01")
    output_old = unfriendly_data_cleaner('2023season_race_stats.csv')
    pprint(output_old)
    print("__________")
    
    print("Question02")
    output_new = pandas_data_cleaner('2023season_race_stats.csv')
    pprint(output_new)
    print("__________")

    ##This is for helping you debug##
    ans = pd.DataFrame(data = output_old[1:], columns = output_old[0]).equals(output_new)
    print(f"Does Q1 output match Q2 output? - {ans}")
    if (not ans):
        print("\nThis is a dataframe that shows where your Q1 matches Q2, and where it doesn't.\nIt will be helpful in debugging:\n")
        ## NOTE: it is sometimes helpful to look at the entire dataframe, to do so, uncomment the next two lines
        # pd.set_option('display.max_rows', None)  # Shows all rows
        # pd.set_option('display.max_columns', None)  # Shows all columns
        print(pd.DataFrame(data = output_old[1:], columns = output_old[0]) == output_new)
    print("__________")

    print("Question03")
    pprint(place_finder(output_new, "Ferrari"))
    print("__________")
    
    print("Question04")
    pprint(left_behind(output_new))
    print("__________")
    
    print("Question05")
    print(stat_summary(output_new))
    print("__________")

    print("Question06")
    print(converted_laps(output_new))
    print("__________")

    print("Question07")
    print(TrackPerformance(output_new))