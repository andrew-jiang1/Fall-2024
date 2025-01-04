# CS 2316 - Fall 2024 - HW01 Python Fundamentals
# HW01: This homework is due by Wednesday, September 4th @ 11:59PM through Gradescope

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - DO NOT import modules within functions
#   - DO NOT leave any print statements within your functions
#   - DO NOT leave 'pass' in your functions
#   - Submit in Gradescope as HW01.py  - Your submission should be named exactly HW01.py

def welcome_class():
    """
    Question 0
    Print the exact string, "Welcome to CS2316!"

    THIS SHOULD BE DONE IN ONE LINE

    >>> welcome_class()
    'Welcome to CS2316!'

    """
    return print('Welcome to CS2316!')

def oddFlow(ingredients):
    """
    Question 1

    This year, Dr. Pepper is introducing a new drink called Oddflow that contains specific ingredients.
    From the list of ingredients provided in the argument, return a string that includes all the ingredients with an odd length.
    Use the phrase ' mixed with ' between each ingredient.
    
    THIS SHOULD BE DONE IN ONE LINE

    Args:
        ingredients (list)
    Returns:
        str
    
    >>> oddFlow(["cherry", "vanilla", "licorice", "almond", "plum", "lemon", "nutmeg", "pepper", "amaretto", "ginger"])
    'vanilla mixed with lemon'

    >>> oddFlow(["cola", "cinnamon", "juniper", "orange", "rootbeer", "birch", "cardamom", "mace", "sassafras", "licorice"])
    'juniper mixed with birch mixed with sassafras'

    """
    return ' mixed with '.join([ingredient for ingredient in ingredients if len(ingredient) % 2 == 1])

def mystery(flavors):
    """
    Question 2

    You have just receieved a list of the 23 mystical flavors of Dr. Pepper, but you, as the biggest Dr. Pepper fan, 
    feel like there's something missing. 

    Args:
        flavors(tuple)
    Returns:
        list

    Using the tuple given, add the flavor "white pepper". 
    Then organize it by sorting the flavors in reverse alphabetical order (by the last letter of each flavor)
    Finally return this as a list

    mystery(flavors = (
        "amaretto", "almond", "blackberry", "black licorice", "caramel", "carrot", 
        "cherry", "clove", "cola", "ginger", "juniper", "lemon", "molasses", "nutmeg", "orange", 
        "prune", "plum", "pepper", "root beer", "rum", "raspberry", "tomato", "vanilla"
    ))
    >>> ('blackberry', 'cherry', 'raspberry', 'carrot', 'molasses', 'ginger', 'juniper', 'pepper',
     'root beer', 'white pepper', 'amaretto', 'tomato', 'lemon', 'plum', 'rum', 'caramel', 'nutmeg', 
     'black licorice','clove', 'orange', 'prune', 'almond', 'cola', 'vanilla')
    """

    lst = list(flavors)
    lst.append("white pepper")
    return sorted((lst),reverse = True, key = lambda w:w [-1])
    
    


def preferences(form):
    """
    Question 3

    The TAs and Dr. McDaniel are planning a party! Everyone submits their favorite drink into a dictionary format.
    The drink of their choice is the key, and the list of names of the people who would like it are the values. Now, 
    everyone need your help to buy the items. 

    Create a dictionary that has the drinks as the keys but the values as a list of two items: 
    - the number of people in the list (as an integer)
    - whether Dr. McDaniel is in the list or not (as a boolean)

    {drink : [name, boolean]}

    Args:
        form(dict)
    Returns:
        dict

    preferences({"Lemonade": ["Anna"], "Coke": ["Brandone", "Sami"], "Sprite":["Christine", "Athena"], 
    "Dr. Pepper":["Sam", "Felipe", "William"], "Water": ["Jeremy", "Dr. McDaniel"]})
    >>> {'Lemonade': [1, False], 'Coke': [2, False], 'Sprite': [2, False], 'Dr. Pepper': [3, False], 'Water': [2, True]}

    preferences({"Lemonade": ["Madison", "Dr. McDaniel"], "Coke": ["Brayden", "Shayna"], "Sprite":["Liv", "Emily", "Lexi"], 
    "Dr. Pepper":["Pablo"], "Water": ["Jacob"]})
    >>> {'Lemonade': [2, True], 'Coke': [2, False], 'Sprite': [3, False], 'Dr. Pepper': [1, False], 'Water': [1, False]}
    """
    shopping_list = {}
    
    for drink in form:
        names = form[drink]
        number = len(names)

        if "Dr. McDaniel" in names:
            in_list = True
        else: 
            in_list = False


        shopping_list[drink] = [number,in_list]
    return shopping_list



    





def sweet_secrets(flavors,measurements):
    """
    Question 4

    You have just found a list containing the Dr Pepper secret formula, but it is currently split into a list of flavors and a list of measurements. 
    Recreate it by combining these two lists into a dictionary where the flavor is the key and its measurement is the value. 
    Only include flavors with an even number of letters.
    
    THIS MUST BE DONE IN ONE LINE

    Args:
        flavors (list)
        measurements (list)
    Returns:
        dict

    Ex: 
    ["cola", "cherry", "licorice", "vanilla", "lemon", "pepper", "ginger", "molasses", "caramel"]
    [0.25, 1.25, 0.66, 0.50, 1.05, 0.20]
    Returns:
    {'cola': 0.25, 'cherry': 1.25, 'licorice': 0.66, 'pepper': 0.5, 'ginger': 1.05, 'molasses': 0.2}

    """
    
    return {flavors:measurements for flavors,measurements in zip((flavors for flavors in flavors if len(flavors) % 2 == 0),measurements) }

    #{expression1:expression2 for item in iterable if expression3 }

def remove_diets(TA_list, McDaniel_list):

    """
    Question 5

    You have been tasked to buy the drinks for a super fun 2316 party, but both the TAs and McDaniel have given
    you a different grocery list, each containing delicious,thirst quenching Dr Pepper products. 
    Return a combined list of every unique product you need to buy.
    Exclude any Diet product, and sort by the first letter in descending order

    THIS QUESTION MUST BE COMPLETED IN ONE LINE

    Args:
        TA_list (list)
        McDaniel (list)
    Returns:
        list
    
    Ex:
    ["Dr Pepper", "Diet Dr Pepper", "Dr Pepper Zero Sugar", "Dr Pepper Strawberries and Cream", "Dr Pepper Cherry Zero Sugar", "Caffeine Free Dr Pepper"]
    ["Dr Pepper", "Dr Pepper Strawberries and Cream", "Dr Pepper Cherry Zero Sugar", "Caffeine Free Dr Pepper", "Cherry Vanilla Dr Pepper", "Dr Pepper and Cream Soda Zero Sugar"]
    Returns:
    ['Dr Pepper and Cream Soda Zero Sugar', 'Dr Pepper Zero Sugar', 'Dr Pepper Strawberries and Cream', 
    'Dr Pepper Cherry Zero Sugar', 'Dr Pepper', 'Cherry Vanilla Dr Pepper', 'Caffeine Free Dr Pepper']
    """
    
    return sorted({x for x in TA_list + McDaniel_list if "Diet" not in x},reverse=True)
    
    
    

def topFlavors(flavors):
    """
    Question 6

    For some reason, Dr. Pepper is bored and wants a dictionary for its top-performing flavors.
    They want the key to be the name of the beverage and the value to be the position in the list squared.
    * Note: The position for the first flavor should be 1, not 0.
    
    THIS SHOULD BE DONE IN ONE LINE

    Args:
        flavors (str)
    Returns:
        dict

    >>> topFlavors('Original, Cherry, Vanilla Float, Cream Soda, Zero Sugar')
    {'Original': 1, 'Cherry': 4, 'Vanilla Float': 9, 'Cream Soda': 16, 'Zero Sugar': 25}
    
    >>> topFlavors('Cherry Vanilla, Diet, Zero Sugar, Dark Berry)
    {'Cherry Vanilla': 1, 'Diet': 4, 'Zero Sugar': 9, 'Dark Berry': 16}

    """
    
    return {l : (pos+1)**2 for pos, l in enumerate(flavors.split(", "))}
   


def sharing_is_caring(friend_list, numCans):
    """
    Question 7

    You LOVE Dr Pepper, and you want to gift all your friends with an ice cold one.
    Given a list of your friends, and a number of ice cold cans you have,
    return the number of cans each person will recieve 

    It is fine for this number to include decimals,as you an pour a can into seperate glasses
    but if so please round to the 100th place (.00)

    If division by zero would occour, return "Oh no!! You broke the rules of math"
    If any other error would occour, return "The Dr would like to speak with you"

    Args:
        friend_list (list)
        numCans
    Returns:
        str

    HINT -> try/except may be useful here, see the handout for more details

    >>>sharing_is_caring(['Christine','Athena','Brandone','Jacob','Your mother','Anna'], 10000)
    1666.67
    
    >>>sharing_is_caring([], 0)
    "Oh no!! You broke the rules of math"

    """
    
    numpeople = len(friend_list)
    

    try:
        cans = int(numCans)
        return float(round(cans/ numpeople,2))
    except: 
        if numCans == 0:
            return "Oh no!! You broke the rules of math"
        return "The Dr would like to speak with you"
        

if __name__ == "__main__":  

## Question 0
     welcome_class()

## Question 1
     print(oddFlow(tuple(["cherry", "vanilla", "licorice", "almond", "plum", "lemon", "nutmeg", "pepper", "amaretto", "ginger"])))
     print(oddFlow(["cola", "cinnamon", "juniper", "orange", "rootbeer", "birch", "cardamom", "mace", "sassafras", "licorice"]))
    
# ## Question 2
     print(mystery(flavors = (
         "amaretto", "almond", "blackberry", "black licorice", "caramel", "carrot", 
         "cherry", "clove", "cola", "ginger", "juniper", "lemon", "molasses", "nutmeg", "orange", 
         "prune", "plum", "pepper", "root beer", "rum", "raspberry", "tomato", "vanilla")))
    
 ## Question 3
     print(preferences({"Lemonade": ["Anna"], "Coke": ["Brandone", "Sami"], "Sprite":["Christine", "Athena"], 
     "Dr. Pepper":["Sam", "Felipe", "William"], "Water": ["Jeremy", "Dr. McDaniel"]}))

     print(preferences({"Lemonade": ["Madison", "Dr. McDaniel"], "Coke": ["Brayden", "Shayna"], "Sprite":["Liv", "Emily", "Lexi"], 
     "Dr. Pepper":["Pablo"], "Water": ["Jacob"]}))
 
 ## Question 4
     print(sweet_secrets(["cola", "cherry", "licorice", "vanilla", "lemon", "pepper", "ginger", "molasses", "caramel"], [0.25, 1.25, 0.66, 0.50, 1.05, 0.20]))

 ## Question 5
     print(remove_diets(["Dr Pepper", "Diet Dr Pepper", "Dr Pepper Zero Sugar", "Dr Pepper Strawberries and Cream", "Dr Pepper Cherry Zero Sugar", "Caffeine Free Dr Pepper"],["Dr Pepper", "Dr Pepper Strawberries and Cream", "Dr Pepper Cherry Zero Sugar", "Caffeine Free Dr Pepper", "Cherry Vanilla Dr Pepper", "Dr Pepper and Cream Soda Zero Sugar"]))

 ## Question 6
     print(topFlavors('Original, Cherry, Vanilla Float, Cream Soda, Zero Sugar'))
     print(topFlavors('Cherry Vanilla, Diet, Zero Sugar, Dark Berry'))

# Question 7
     print(sharing_is_caring(['Christine','Athena','Brandone','Jacob','Your mother','Anna'], 10000))
     print(sharing_is_caring([], 0))