
import json



'''

adict = json.load(open("book.json"))
print(adict)
'''

# Lecture 5 Example 1

'''
adict = json.load(open("skywalker.json"))
bdict = {key:value for key,value in adict.items 
if key not in ["hair_color","eye_color","skin_color"]}

json.dump(bdict, open("skywalker.json","w"))
'''

#Lecture 5 Coding Exercise
'''

def get_keys(file):
	adict = json.load(open(file))
	return adict.keys()

print(get_keys("book.json"))
'''

alist = [None, 125, 2.5]

newstr = json.dumps(alist)

print(newstr[2])

