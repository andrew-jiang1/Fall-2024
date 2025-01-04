import re

# Lecture 8 Example 1

'''

text = """My phone number is 770-333-5678 and Anna's phone number is 404-404-1111 and Athena's phone number is 678-422-5678"""

pref_list = re.findall((r" (\d\d\d)-"),text) # The inner parentheses tells the code that it only wants to keep the 3 digit and not the hyphen
print(pref_list) # putting the r before the pattern makes it a raw pattern so that a pattern such as \n can be recognized instead of a new line

'''

#Lecture 8 Example 2

'''

text = "<people><person><Turing>"

tag_list = re.findall("<(.+)>",text) # This shows that it's regex is inherently greedy because it goes for the longest possible string

print(tag_list)

'''

# Lecture 8 Example 3 # Maybe a Test Question

'''

html_text = '<li>Coffee</li><li>Tea</li><br><br><br><img src="totoro.jpg" /img><li>Milk</li>' # Trace around the values we want, then write regex to find it

print(re.findall("<li>(.+?)</li>",html_text))

print(re.findall(r'="(.+\.jpg)',html_text)) # Since totoro.jpg has . we have to put \ in front of it to stop it from just doing all characters instead

'''

# Lecture 8 Example 5 
'''

text = """My phone number is 770-333-5678 and Anna's phone number is 404-404-1111 and Athena's phone number is 678-422-5678"""

my_match =re.search(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)",text) # you are allowed separate groups

my_match_list =re.finditer(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)",text) # you are allowed separate groups

prefix_list = [my_match.group(1) for my_match in my_match_list]

'''
"""

print(my_match.group()) # group gives you the text that matched
print(my_match.group(1)) # if you have multiple groups it will split it up starting with the first instance then moving onward
print(my_match.group(2))

print(my_match.group(3))

"""

# Lecture 8 Coding Exercise

'''

chat = "Athena:Hi queen <3\nAnna:heyyy what's up?\nAthena: are you coming to lecture?\nAnna:moved to Wednesdays!\n"

print(re.search(r":(.+\?)",chat).group(1))

'''

# Lecture 8 Example 6

text = "I love CS2316."

new_string = re.sub(r"[ \d\.]","$",text)

print(new_string)
