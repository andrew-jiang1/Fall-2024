'''
def three_smallest(alist):
	return sorted(alist)[0:3]



print(three_smallest([5,2,4,1,7]))
#should print out [1,2,4]
'''


'''
def build_dict(list1,list2):
	final_dict = {}
	shortest_length = len(list_1) if len(list_1) < len(list_2) else len(list_2)
	for i in range(shortest_length):
		final_dict([ist_1[i]] = list_2[i]
	return final_dict

print(build_dict([1,2,3],[4,5,6]))
# should print out (1: 4, 2: 5, 3: 6)
'''


'''
def get_initials(list):
	list2 = []
	for i in list:
		initial = ""
		split = i.split()
		for j in split:
			initial += j[0]
		list2.append(initial)
	return list2

print(get_initials(["Tom Brown", "Sarah Li", "Pedro Diego"]))
'''

'''
print(list(zip([1,2,3],(4,5,6))))
'''


print(dict(zip([1,2,3],[4,5,6,7,8])))


'''
city_list = ["Chicago","Atlanta","Chicago"]
print(sorted(list(set(city_list))))
'''
