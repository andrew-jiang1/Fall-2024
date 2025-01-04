# Lecture 4 Example 1

# 


list2 = [num/2 if num%2==0 else num*2 for num in range(-10,11) if num != 0]
print(list2)



with open("course_schedule.txt") as f:
    text = f.read()
print(text[0:500])


# Lecture 4 Example 2

'''
def get_1000(fname1,fname2):

    cwith open(fname1,"r") as infile:
        text = infile.read()
    with open(fname2,"w") as outfile:
        outfile.write(text[:1000])


get_1000("course_schedule.txt", "course_schedule_1000.txt")
'''

# Lecture 4 Example 2.5

'''
with open("country__happiness.csv") as infile:
    data = infile.readlines()
    data = data[1:] # remove header line
print(data[1])

for line in data:
    pieces = line.split(",")
    if pieces[0] == "AT":
        print(pieces[2])
'''

'''
import csv

with open("country__happiness.csv") as f:
    reader = csv.reader(f, delimiter = ",", quotechar = '"')
    reader_list = list(reader) # a list of listste
#print(reader_list[:3])
for line in reader_list:
    if line[0] == "AT":
        print(line[2])
'''


# Lecture 4 Example 3re

'''

import csv

with open("countries.csv") as f:
    reader = csv.reader(f)
    reader_list = list(reader)
    reader_list = reader_list[1:]
count = 0
for line in reader_list:
    if "europe" in line[1].lower():
        count += 1:
print(count)

'''

# Ex 4

'''

headers = ["Name","Age","GPA"]
data_list = [["Will",20,4.0],["Christina",21,4.0],["Anna",21,4.0]]


with open("ta_list.csv","w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    writer.writerows(data_list)

'''

#Coding Exercise

'''
import csv

def convert_file(file1,file2):
    with open(file1,"r") as infile:
        reader = csv.reader(infile)
        reader_list = list(reader)
    headers = reader_list[0]
    with open(file2, "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        for line in reader_list:
            if line[0][0] == "A":
                writer.writerow(line)

convert_file("countries.csv", "a_countries.csv")
'''

        
