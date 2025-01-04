# CS 2316 - Fall 2024 - HW02
# HW02: This homework is due by September 15th @ 11:59PM through Gradescope

# This homework is divided into three sections.
# Questions 1, 2, and 3 require you to download the "2023season_drivers.txt" file as they are linked questions. 
                        # Please comment out Q1 when you run Q2 and Q3
# Questions 4, 5, and 6 require you to download the "2023season_race_stats.csv" file 

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW02.py  - Your submission should be named exactly HW02.py

# 2023season_drivers.txt and 2023season_race_stats.csv must be located in the same folder as HW02.py in order for your code to run properly

import json, csv
from pprint import pprint

def winner_winner(txtFile, country):
    """
    Question 01

    2023season_drivers.txt contains information on all F1 drivers during the 2023 season.
    We are interested in extracting the following information for drivers that were born in the country specified in the 
    inputted 'country' parameter.
        1. Driver's Name
        2. Highest Race Finish
        3. Place of Birth
            - Note that in the file the Place of Birth is enclosed in double quotations
            - Make sure to remove any excess quotations
    Return a list of lists of [Driver, Highest Race Finish, Place of Birth] for each driver born in the specified country.

    Args:
        txtFile (2023season_drivers.txt)
        country (string)
    Returns:
        list of lists

    >>> pprint(winner_winner('2023season_drivers.txt', 'England'))
    [['Lewis Hamilton', '1(x103)', 'Stevenage, England'],
     ['Lando Norris', '2(x7)', 'Bristol, England'],
     ['George Russell', '1(x1)', "King's Lynn, England"],
     ['Alexander Albon', '3(x2)', 'London, England']]

    >>> pprint(winner_winner('2023season_drivers.txt', 'Belgium'))
    [['Max Verstappen', '1(x54)', 'Hasselt, Belgium']]
    """
    
    info = []
    with open(txtFile,"r") as f:
        reader = f.readlines()
        reader_list = list(reader[1:])
    
    for line in reader_list:
        lines = line.split("\t")
        check = lines[12]
        frame = check[1:len(check)-2]
        home = frame.split(", ")

        if home[1] == country:
            driver_name = lines[0]
            hrf = lines[9]
            birth = frame
            info.append([driver_name,hrf,birth])
        
        
    
    return info
    




        
        

def write_to_json(file):
    '''
    Question 02
    - Using file I/O to access the given file, create a dictionary where each key in the dictionary is a driver's name
    - The value should be the name abbreviation associated with each driver
    - Only use information from every OTHER line, excluding the starting line. (That is, lines 1, 3, 5, ...)
    - Write the dictionary to a JSON file with the name of "abbrevs.json"
    - Return the dictionary
    - You MUST use file I/O

    Args:
        file (2023season_drivers.txt)
    Returns:
        dictionary
        
    Output:
        {'Alexander Albon': 'ALB',
         'Carlos Sainz': 'SAI',
         'Charles Leclerc': 'LEC',
         'Daniel Ricciardo': 'RIC',
         'Kevin Magnussen': 'MAG',
         'Lewis Hamilton': 'HAM',
         'Logan Sargeant': 'SAR',
         'Max Verstappen': 'VER',
         'Oscar Piastri': 'PIA',
         'Pierre Gasly': 'GAS',
         'Valtteri Bottas': 'BOT'}
    '''
    
    dict = {}
    with open(file, "r") as f:
        text = f.readlines()
        lst = list(text[1::2])

        for line in lst:
                lines = line.split("\t")
                name = lines[0]
                abb = lines[1]
                dict.update({name:abb})
    
    with open("abbrevs.json","w") as outfile:
        json.dump(dict,outfile)
        
    return dict

        
def driver_teams(input_txt_file):
    """
    Question 03

    Your friend is unfamiliar with Formula 1 and you want to make them a dictionary of all 
    of the teams and the players on each of them. Using 2023season_drivers.txt, create a 
    dictionary with the teams as the key and the list of drivers on the team as the value.
    Return the dictionary AND write it to a JSON file named "teams.json".

    HINT: THERE ARE NO DUPLICATE NAMES

    Args: 
        input_txt_file (2023season_drivers.txt)
    Returns:
        dictionary of lists

    >>> pprint(driver_teams("2023season_drivers.txt"))
    {'Alfa Romeo': ['Valtteri Bottas', 'Guanyu Zhou'],
        'AlphaTauri': ['Yuki Tsunoda',
                'Daniel Ricciardo',
                'Liam Lawson',
                'Nyck De Vries'],
        'Alpine': ['Pierre Gasly', 'Esteban Ocon'],
        'Aston Martin': ['Fernando Alonso', 'Lance Stroll'],
        'Ferrari': ['Charles Leclerc', 'Carlos Sainz'],
        'Haas F1 Team': ['Nico Hulkenberg', 'Kevin Magnussen'],
        'McLaren': ['Lando Norris', 'Oscar Piastri'],
        'Mercedes': ['Lewis Hamilton', 'George Russell'],
        'Red Bull Racing': ['Max Verstappen', 'Sergio Perez'],
        'Williams': ['Alexander Albon', 'Logan Sargeant']}
    """
    dict = {}
    with open(input_txt_file) as f:
        txt = f.readlines()
        every = list(txt[1:])
        
        for line in every:
            sline = line.split("\t")
            name = sline[0]
            team = sline[3]
            if team not in dict:
                dict[team] = [name]
            else:
                dict[team].append(name)

    with open("teams.json","w") as out:
        json.dump(dict,out)
            
    return dict

def friendly_data_cleaner(input_file):
    """
    Question 04
    
    You have been given a csv file with information about the 2023 F1 season! Complete data! So exciting! 
    The person who made the data messed up, and it's kind of hard to work with. Since you're such a nice
    person, you volunteered to help them clean up the data. Here's everything that they want you to do:
    
    1. There are two identical driver columns and two idential team columns with different column
        names, drop the ones with the _Dup suffix
    2. Replace all empty values in Q1, Q2, and Q3 as 'N/A'
    3. Drop all rows that contain DNF or DNS in Q1, Q2, and Q3
    4. Rename Q1, Q2, and Q3 to 'Qualifying 1', 'Qualifying 2', and 'Qualifying 3'
    5. Split the driver's names into two columns. Rename the original 'Driver' column into 'Driver First Name' and 
        'Driver Last Name' at the same index.
    6. Replace occurence of 'Alfa Romeo Ferrari' with 'Kick Sauber Ferrari'
    7. Create a new column called "Engine Manufacturer" right after the team name column populated with the
        last word of each team name. If the team name is only one word, duplicate it.
    
    Write the data out to a csv file called 'clean_2023season_stats.csv' and return the list of lists
    
    YOU MUST DO THIS QUESTION FOR HOMEWORK 05 
    
    HINT: USE .INSERT()

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

        # Part 1 Removing _Dup suffix
        
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

        # Part 2 Replace empty values in Q1-Q3 with N/A

        for row in nrs:
            row[q1] = row[q1] if row[q1] else "N/A"
            row[q2] = row[q2] if row[q2] else "N/A"
            row[q3] = row[q3] if row[q3] else "N/A"
            
        # Part 3 Drop all rows that contain DNF or DNS in Q1-Q3  
        
        cr = []
        for row in nrs:
            if "DNF" not in [row[q1],row[q2],row[q3]] and "DNS" not in [row[q1],row[q2],row[q3]]:
                cr.append(row)

        # Part 4 Replacing Headers Q1 - Q3 with new header names

        nh[q1] = "Qualifying 1"
        nh[q2] = "Qualifying 2"
        nh[q3] = "Qualifying 3"    
            
        # Part 5 Split Driver name into First Name and Last Name in the same index

        driver_name = nh.index("Driver")
        nh[driver_name] = "Driver First Name"
        nh.insert(driver_name+1,"Driver Last Name")

        for row in cr:
            fname = row[driver_name].split(" ",1)
            row[driver_name] = fname[0]
            row.insert(driver_name + 1 , fname[1])
        
        # Part 6 Replace Occurence of Alfa Romeo Ferrari with Kick Sauber Ferrari

        tpos = nh.index("Team")
        for row in cr:
            if row[tpos] == "Alfa Romeo Ferrari":
                row[tpos] = "Kick Sauber Ferrari"

        # Part 7 Create a new column called Engine Manufacturer populated with the last word of each team name. If team name is only one word, duplicate it
        
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

def team_stats(input_file):
    '''
    Question 05
    
    Using your "clean_2023season_stats" csv file from Question 04, we want to look at each of the teams
    competing in F1 during the 2023 season. Specifically, we want to have a list called "Drivers" of 
    all the drivers that were at one point on the team during the season sorted in alphabetical order, 
    and the total number of points earned by the team.

    
    Args:
        input_file (clean_2023season_stats.csv)
    Returns:
        dictionary of dictionaries

    >>> pprint(team_stats('clean_2023season_stats.csv'))
    
    {'AlphaTauri Honda RBPT': {'Drivers': ['Daniel Ricciardo',
                                        'Liam Lawson',
                                        'Nyck De Vries',
                                        'Yuki Tsunoda'],
                            'Total Points': 22},
     'Alpine Renault': {'Drivers': ['Esteban Ocon', 'Pierre Gasly'],
                            'Total Points': 109},
     ...
     'Williams Mercedes': {'Drivers': ['Alexander Albon', 'Logan Sargeant'],
                            'Total Points': 25}}
    '''
    
    team_dict = {}

    with open("clean_2023season_stats.csv","r") as f:
        reader = csv.reader(f)
        ls = list(reader)
        head = ls[0]

        dfiname = head.index("Driver First Name")
        dlaname = head.index("Driver Last Name")
        tea = head.index("Team")
        point = head.index("Points")
        for row in ls[1:]:
            te = row[tea]
            dfuname = row[dfiname] + " " + row[dlaname]
            points = int(row[point])

            if te not in team_dict:
                team_dict[te] = {"Drivers": [], "Total Points" : 0}
            
            if dfuname not in team_dict[te]["Drivers"]:
                team_dict[te]["Drivers"].append(dfuname)
            
            team_dict[te]["Total Points"] += points

            for te in team_dict:
                team_dict[te]["Drivers"].sort()
            


    return team_dict

def track_stats(input_file):
    """
	Question 06
		
	Using your "clean_2023season_stats" csv file from Question 04, we want to take a closer look into 
    the change in driver positions for each track.
	Create a dictionary categorizes the number of changes between each drivers' starting grid position and their 
    ending positions ('Position') into keys of 'Negative Change', 'No Change', 'Positive Change', and 
    'No Placement' if the driver did not finish the race ('NC') or was disqualified ('DQ') for each race.
    For each race, we also want to find out which driver had the fastest lap time for each race, and add their name
    to the dictionary——but if the fastest driver was removed in Question 04, then that race will not have anyone
    labelled as "Fastest Driver". If no one ended up with a 'NC' or 'DQ,' there will not be a 'No Placement category.

	The values should be an inner dictionary of the count of each change interval in each of the different tracks.

    Args:
        input_file (clean_2023season_stats.csv)
    Returns:
        dictionary of dictionaries

	>>> pprint(track_stats('clean_2023season_stats.csv'))
    
    {'Abu Dhabi': {'Fastest Driver': 'Max Verstappen',
               'Negative Change': 7,
               'No Change': 6,
               'Positive Change': 6},
     'Australia': {'Negative Change': 4,
               'No Change': 2,
               'No Placement': 3,
               'Positive Change': 10},
     ...
     'United States': {'Fastest Driver': 'Yuki Tsunoda',
                   'Negative Change': 2,
                   'No Change': 2,
                   'No Placement': 5,
                   'Positive Change': 11}}
    
    """
    
    track_dict = {}

    with open("clean_2023season_stats.csv","r") as f:
        reader = csv.reader(f)
        tls = list(reader)
        hea = tls[0]

        track_name = hea.index("Track")
        starting_pos = hea.index("Starting Grid")
        pos = hea.index("Position")
        finame = hea.index("Driver First Name")
        laname = hea.index("Driver Last Name")
        fastlap = hea.index("Fastest Lap Time")
        setlap = hea.index("Set Fastest Lap")

        for ro in tls[1:]:
            tra = ro[track_name]
            funame = ro[finame] + " " + ro[laname]
            start = ro[starting_pos]
            position = ro[pos]
            fastest = ro[fastlap]
            setl = ro[setlap]

            if tra not in track_dict:
                track_dict[tra] = {}
            
            if position == "NC" or position == "DQ":
                if "No Placement" not in track_dict[tra]:
                    track_dict[tra]["No Placement"] = 0
                track_dict[tra]["No Placement"] += 1
            
            else:
                rstart = int(start)
                rposition = int(position)

                if rposition > rstart:
                    if "Negative Change" not in track_dict[tra]:
                        track_dict[tra]["Negative Change"] = 0
                    track_dict[tra]["Negative Change"] += 1
                elif rposition == rstart:
                    if "No Change" not in track_dict[tra]:
                        track_dict[tra]["No Change"] = 0
                    track_dict[tra]["No Change"] += 1
                else:
                    if "Positive Change" not in track_dict[tra]:
                        track_dict[tra]["Positive Change"] = 0
                    track_dict[tra]["Positive Change"] +=1

            if setl == "Yes" and funame:
                track_dict[tra]["Fastest Driver"] = funame

    return track_dict






if __name__ == "__main__":
    print("Question01")
    pprint(winner_winner('2023season_drivers.txt', 'England'))
    pprint(winner_winner('2023season_drivers.txt', 'Belgium'))
    print("__________")
    
    print("Question02")
    pprint(write_to_json("2023season_drivers.txt"))
    print("__________")

    print("Question03")
    pprint(driver_teams("2023season_drivers.txt"))
    print("__________")
    
    print("Question04")
    pprint(friendly_data_cleaner('2023season_race_stats.csv'))
    print("__________")
    
    print("Question05")
    pprint(team_stats('clean_2023season_stats.csv'))
    print("__________")

    print("Question06")
    pprint(track_stats('clean_2023season_stats.csv'))
    print("__________")