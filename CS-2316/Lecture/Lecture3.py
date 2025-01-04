"Lecture 3 Example 1"

'''
print(sorted("the cat is brown".split(),key = lambda w:w[-1]))
'''

"Lecture 3 Example 2"

'''
def record_result(num1,num2):
    return "Record Broken!" if num1 < num2 else "Record remains unchanged"
    
print(record_result(2.31,2.32))
'''

# Lecture 3 Coding Exercise

# set the list to variable w for lambda, split the values in the variable which would be the list values, then pull the values of the index
# [0][-1] to check for the first name of the list, then you check for the last letter of the first name

'''
def weird_sort(alist):
    return sorted((alist),key = lambda w:w.split()[0][-1])

print(weird_sort(["Sam Walls", "Athena Malek", "Sami Mathew"]))
'''

# Lecture 3 Example 3

'''
alist = [x for x in "Jackets" if x not in ["a","e","i","o","u"] and not x.isupper()]
print(alist)
'''

# Lecture 3 Example 4

"""

newdict = {l : l.upper() for l in "jackets"}
print(newdict)

"""

#Lecture 3 Example 5

'''
newdict = { l : pos for pos,l in enumerate("jackets")}
print(newdict)
'''

