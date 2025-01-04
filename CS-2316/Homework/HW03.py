# CS 2316 - Fall 2024 - HW03
# HW03: This homework is due by September 29th @ 11:59PM through Gradescope

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW03.py  - Your submission should be named exactly HW03.py

from pprint import pprint
from bs4 import BeautifulSoup
import requests
import re 

def planet_finder(planets):
    """
    Question 01 

    You are in charge of designing a new planet for an upcoming Star Wars show! To get ideas you want to look at real planets!
    Given a long string, you need to check if the first one is a planet following the pattern (word,number,'b')
    
    If it is, return this planet, otherwise, return "This is not the planet you're looking for"  

    YOU MUST USE REGEX FOR THIS QUESTION

    Args:
        planets (str)
    Returns:
        str


    >>> print(planet_finder('Gliese 12 b Gliese 229 .... TRAPPIST-1g Wolf 1069 b Wolf 1061c'))
    'Gliese 12 b'
 
    >>> print(planet_finder('TRAPPIST-1g Wolf 1069 b Wolf 1061c'))
    'This is not the planet you're looking for'

    """
    text = planets
    match_text = re.match(r'[A-z]+ \d+ b',text)
    if match_text != None:
        return match_text.group()
    else:
        return "This is not the planet you're looking for"



def find_my_droid(radar):
    """
    Question 02

    In a galaxy far far away, we're on the hunt for our droids! Unfortunately, we have lost them, and they're mixed up in a list
    of everyone we know.

    Write a fuction using regex that will find the first droid for you to use. Droids have capital letters or numbers, a possible
    dash, and more capital letters or numbers.

    Args:
        radar (str)
    Returns:
        str

    print(find_my_droid('Leia, Luke, C1-10P, Ahsoka, K-2S0, Echo, R2-D2, Tech, R4, IG-88, BB-8, Omega, C-3P0'))
    >>>>> 'C1-10P'

    print(find_my_droid('Ahsoka, Echo, R2-D2, Tech, R4, IG-88, BB-8, Omega, C-3P0'))
    >>>>> 'R2-D2'

    """

    return re.search("[A-Z]+\d+-?[A-Z]*\d*[A-Z]*",radar).group()


def crossover_time(exo_planets, scifi_planets):
    """
    Question 03
    
    You are curious about which real exo-planets some of your favorite sci-fi planets are based off of, to do this you
    substitute their sci-fi names, in place of their real names.

    Return a list with the sci-fi planets subsitiuted for their real counterparts. 
    Both lists will be the same length.

    THIS MUST BE DONE IN ONE LINE USING REGEX

    Args:
        scifi_planets(list), exo_planets(list)
    Returns:
        list

    
    >>> print(crossover_time(["Kepler-62f's mass is 2.8+0.4−0.4 earths. Kepler-62f's radius is 1.41 earths, and it is located only 981 light years from earth.",
    "TRAPPIST-1g's mass is 1.32 earths. TRAPPIST-1g's radius is 1.13 earths, and it is located only 41 light years from earth.",
    "Wolf 1061c's mass is ≥3.41 earths. Wolf 1061c's radius is ~1.60 earths, and it is located only 13.8 light years from earth."],
    ["Yavin", "Caladan", "Reach"]))

    
    ["Yavin's mass is 2.8+0.4−0.4 earths. Yavin's radius is 1.41 earths, and it is located only 981 light years from earth.',
    "Caladan's mass is 1.32 earths. Caladan's radius is 1.13 earths, and it is located only 41 light years from earth.',
    "Reach's mass is ≥3.41 earths. Reach's radius is ~1.60 earths, and it is located only 13.8 light years from earth.']

    """
    
    return [re.sub(r"(\w*[\s|-]\w*)'",exo_planets+"'",scifi_planets) for exo_planets,scifi_planets in zip(scifi_planets,exo_planets)]

    
def bday_plans(planets):
    """
    Question 04 

    Keeping the trend of sorting planets, let's go to a galaxy far far away!
    Han Solo wants to throw a birthday party and needs to invite his friends. For some reason, they reside in the planets located south of 
    every double lettered planet (the planet in the list right after the double letter one). 

    Write a function using regex that will produce a list of all planets located directly after any double lettered planet.

    HINT: Use back-referencing and you will need to do some conversion from tuples in lists to your final list

    THIS MUST BE DONE IN ONE LINE  

    Args:
        planets (str)
    Returns:
        List


    >>> pprint(bday_plans('Tatooine, Bespin, Endor, Kamino, Naboo, Hoth, Aldernaan, Geonosis, Coruscant')) 
    ['Bespin', 'Hoth', 'Geonosis']

    """
    return [x[1] for x in re.findall(r'(\w+)\1\w*,\s*(\w+)', planets)]
    

def climate_control():
    """
    Question 05

    An explorer is looking to travel to various planets. But first, he wants to know the possible climates before his trip to know what to pack. 
    Provide a Set of possible climates the explorer might encounter. 
    
    Note: Order does not matter, and some climates may have a comma in them such as "temperate, tropical"

    URL = https://swapi.dev/api/planets

    Args:
        None
    Returns:
        Set
 

    >>> climate_control()
    {'arid', 'temperate, tropical', 'murky', 'frozen', 'temperate'}

    """
    url = "https://swapi.dev/api/planets"
    resp = requests.get(url)
    alist = resp.json()
    climates = set()

    for d in alist["results"]:
        climates.add(d["climate"])

    return climates
        

    




    


def film_planets():
    """
    question 66 

    A film fanatic is looking through all of the Star Wars movies. 
    They want to find information about the various planet appearances in the movies. 

    First, they are only concerned with planets that have a known population greater than 6 million
    Then, they are looking for the name of each movie and the number of unique characters in all of the movies for each associated planet. 
    Finally, using this information, sort your data based on the number of characters in the movies associated with the planet in descending order. 
    If two planets have the same character count, sort by the name of the planet in alphabetical order
    
    URL = https://swapi.dev/api/planets
    
    Args:
        None
    Returns:
        List of Tuples (containing a string and dictionary)


    >>> film_planets()
        [('Coruscant',
          {'num_characters': 75,
           'titles': ['Return of the Jedi',
                      'The Phantom Menace',
                      'Attack of the Clones',
                      'Revenge of the Sith']}),
         ('Naboo',
          {'num_characters': 75,
           'titles': ['Return of the Jedi',
                      'The Phantom Menace',
                      'Attack of the Clones',
                      'Revenge of the Sith']}),
         ('Alderaan',
          {'num_characters': 41, 'titles': ['A New Hope', 'Revenge of the Sith']}),
         ('Kamino', {'num_characters': 40, 'titles': ['Attack of the Clones']}),
         ('Endor', {'num_characters': 20, 'titles': ['Return of the Jedi']})]
    
    
    """
    url =  "https://swapi.dev/api/planets"
    resp = requests.get(url)
    blist = resp.json()
    lst = []

    for p in blist["results"]:
        if p["population"] != "unknown" and int(p["population"]) > 6000000:
            name = p["name"]
            title_list = []
            s = set()

            for furl in p["films"]:
                resp2 = requests.get(furl)
                clist = resp2.json()
                title_list.append(clist["title"])

                for curl in clist["characters"]:
                    s.add(curl)
                
            diction = {"num_characters":len(s),"titles":title_list}
            lst.append((name,diction))
    
    sort = sorted(lst, key = lambda x : (-x[1]["num_characters"],x[0]), reverse = False)
    
    

                
    return sort
    
def the_dark_side(sith):
    """
    Question 07

    sith = https://en.wikipedia.org/wiki/Sith
    
    OH NO you have been seduced to the dark side!! You begin to research all of the Sith masters in order to learn their ways.
    Looking at only the Key People in the table (this includes the key people legends but not affiliates or anything below), put them into a Set.

    Recall, order does not matter in a set.

    Args:
        sith (str)
    Return:
        Set

    >>> print(the_dark_side(sith))
    {'Darth Vader','Darth Sidious','Darth Tyranus','Darth Maul',...'Lady Lumiya'}

    """
    resp = requests.get(sith)
    soup = BeautifulSoup(resp.text,"html.parser")

    masters = set()

    table = soup.find("table",{"class":"infobox"})
    tr = table.find_all("tr")

    for row in tr:
        if row.find("th"):
            h = row
            
            
            
            

    
    


    


    return masters
    

def jedi_finder(url):
    """
    Question 08

    URL = https://en.wikipedia.org/wiki/Jedi

    You've been given a rough chart of the master-apprentice relationships (the chart on the page titled similarly)
    Return a list of all of the Jedi present in this chart, pull the text out of each tag, not the title
    
    NOTE: each Jedi's name should be formatted as you would a normal name, you should only have jedi in this list 
    (and only the ones shown in the chart, this includes 'Younglings', but not 'Jedi order')
    The list should be sorted in alphabetical order 

    Args:
        url (str)
    returns:
        List


    >>> print(jedi_finder(url))
    ['Ahsoka Tano','Anakin Skywalker','Ben Solo',...,'Qui-Gon Jinn','Rey','Sabine Wren','Yoda','Younglings']
    
    """
    resp = requests.get("https://en.wikipedia.org/wiki/Jedi")
    bs = BeautifulSoup(resp.text, "html.parser")
    
    tables = bs.find("table")
    return tables

if __name__ == "__main__":

    print("Question01")
    pprint(planet_finder("Gliese 12 b Gliese 229 Ac Gliese 357 d Kepler-62e GJ 1061 d HD 216520 c HIP 38594 b K2-9b K2-72e Kepler-62f Kepler-155c Kepler-283c Kepler-296e Proxima Centauri b Ross 128 b Ross 508 b Teegarden's Star b Teegarden's Star c Kepler-1649c TOI-700 d TRAPPIST-1g Wolf 1069 b' Wolf 1061c"))
    pprint(planet_finder("Kepler-62e GJ 1061 d HD 216520 c HIP 38594 b K2-9b K2-72e Kepler-62f Kepler-155c Kepler-283c Kepler-296e Proxima Centauri b Ross 128 b Ross 508 b Teegarden's Star b Teegarden's Star c Kepler-1649c TOI-700 d TRAPPIST-1g Wolf 1069 b' Wolf 1061c"))
    print("__________")

    print("Question02")
    print(find_my_droid('Leia, Luke, C1-10P, Ahsoka, K-2S0, Echo, R2-D2, Tech, R4, IG-88, BB-8, Omega, C-3P0'))
    print(find_my_droid('Ahsoka, Echo, R2-D2, Tech, R4, IG-88, BB-8, Omega, C-3P0'))
    print("__________")

    print("Question03")
    pprint(crossover_time(["Kepler-62f's mass is 2.8+0.4−0.4 earths. Kepler-62f's radius is 1.41 earths, and it is located only 981 light years from earth.",
    "TRAPPIST-1g's mass is 1.32 earths. TRAPPIST-1g's radius is 1.13 earths, and it is located only 41 light years from earth.",
    "Wolf 1061c's mass is ≥3.41 earths. Wolf 1061c's radius is ~1.60 earths, and it is located only 13.8 light years from earth."],
    ["Yavin", "Caladan", "Reach"]))
    print("__________")

    print("Question04")
    planets = 'Tatooine, Bespin, Endor, Kamino, Naboo, Hoth, Aldernaan, Geonosis, Coruscant'
    print(bday_plans(planets))
    print("__________")
    
    print("Question05")
    pprint(climate_control())
    print("__________")

    print("Question06")
    pprint(film_planets())
    print("__________")

    print("Question07")
    pprint(the_dark_side("https://en.wikipedia.org/wiki/Sith"))
    print("__________")

    print("Question08")
    pprint(jedi_finder("https://en.wikipedia.org/wiki/Jedi"))
    print("__________")