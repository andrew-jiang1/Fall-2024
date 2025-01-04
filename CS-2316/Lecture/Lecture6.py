import requests

#Lecture 6 Example 1

'''
url = "https://ghibliapi.vercel.app/films"
resp = requests.get(url) #send a request to that website
# print(resp)
print(resp.text[:1000])
alist = resp.json() # this function converts the string # to appropriate data types
print(len(alist))
'''

#Lecture 6 Example 2

'''
url = "https://ghibliapi.vercel.app/films"
resp = requests.get(url) 
alist = resp.json()
print(alist[0])
print(sorted([d["title"] for d in alist ]))
'''

#Lecture 6 Example 3

"""
url = "https://ghibliapi.vercel.app/films"
resp = requests.get(url) 
alist = resp.json()
# print(alist[0].keys())
highest_score = 0
highest_title = ""
for d in alist:
    #print(d["title"],d["rt_score"])
    if int(d["rt_score"]) > highest_score:
        highest_score = int(d["rt_score"]) # Casting it to be a number since the original datatype would be a string
        highest_title = d["title"]
print(f"Best film is {highest_title} with score {highest_score}")
"""

# Lecture 6 Example 4

"""
url = "http://cc.gatech.edu"
r = requests.get(url)
print(r)  # prints the status code only
print(r.text[:1000]) # prints the text
data = r.json()  # converts json text to python
"""

# Lecture 6 Coding Exerise Exercise

'''
url = "https://ghibliapi.vercel.app/films"
resp = requests.get(url) 
alist = resp.json()

print(len([d["title"] for d in alist])) # Part 1 Answer

print(alist[8]["director"]) # Part 2 Answer

s_runtime = 1000
s_title = ""

for d in alist: # Part 3 Answer
    if int(d["running_time"]) < s_runtime:
        s_runtime = int(d["running_time"]) 
        s_title = d["title"]
print(f"The shortest film is {s_title} with a filming run time of {s_runtime}") 
'''



