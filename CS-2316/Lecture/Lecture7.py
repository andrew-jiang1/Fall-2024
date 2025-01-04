# Lecture 7 Example 1
'''

import re
pattern = "George"
text = "Georgia Tech Yellow George" # Still does not match since re.match looks for an exact match so the text can only be George
print ("Match") if re.match(pattern, text) else print("No Match")
'''

#Lecture 7 Example 2

'''
import re
pattern = "Yell"
text = "Georgia Tech Yellow Jackets"
match_obj = re.search(pattern,text)
print(match_obj.start()) if match_obj else print("Not Found")
'''

# Lecture 7 Example 3

'''
import re
pattern = "he"
text = "The text might have multiple matches."
print(len(re.findall(pattern,text))) # For findall, the len function just makes it say how many times it occurs
'''

# Lecture 7 Example 4

'''
import re

pattern = "he"
text = "The text might have multiple matches"
match_obj = re.search(pattern,text)
print(re.finditer(pattern,text))
for match_obj in re.finditer(pattern,text):
    print(match_obj.start())
'''

# Lecture 7 Example 5

'''
import re

text = "Move the desks in rooms 123, 437, 329, 101, and 183."
print(re.findall("[aeiouAEIOU]",text))
'''

#Lecture 7 Example 6

import re
'''
text = "Move the desks in rooms 1236, 487, 1229, 101, and 99"
print(re.findall(" \d\d\d,",text)) # point of the space is to remove any numbers that are 4 digits and it reads the last 3, point of comma is to end it after the first 3
'''

#Lecture 7 Coding Exercise

sentence = "The CS2316 TAs are 9 of my favorite people on Earth."
print(len(re.findall("[a-zA-Z] ",sentence)))

# Lecture 7 Example 7

