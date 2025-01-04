# CS 2316 - Fall 2024 - HW04 Numpy - Ye Olde Minecraft Trading Sim
# HW04: This homework is due by October 6th @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW04.py - Your submission should be named exactly HW04.
#   - Do not create your own test cases, use the ones provided
#   - REPLACE THE PASS STATEMENTS WITH YOUR CODE

import numpy as np
from pprint import pprint
import random

def window_counter(num_windows, length_wall):
	"""
	QUESTION 01

	You are going to build an awesome minecraft house. For your house to be awesome, you need to have windows to let in light.
	You want the windows to be evenly placed throughout the walls in your house. Given the number of windows you want (num_windows) 
	and the length of your wall (length_wall), return an array where each element is the position of a window rounded to the nearest integer.

	THIS MUST BE DONE IN ONE LINE

	HINT:
	- You want your array to include the locations of the windows.
	- You do not want to include the starting index (index = 0) or ending index.

	Args:
		num_windows (int)
		length_wall (int)

	Returns:
		np.array

	>>  pprint(window_counter(4, 50))
	array([ 10, 20, 30, 40])

	"""
	return np.linspace((length_wall / (num_windows+1)),length_wall,num_windows,endpoint= False, dtype = "int64")

def miner_ranker(num_diamonds, num_mines):
	"""
	QUESTION 02

	You and your friends are in a minecraft realm and want to figure out who is the most efficient miner.
	You are given an array containing the total number of diamonds each of your friends has and an array 
	with the number of times they've been mining.
	You want to return an array that shows the average number of DIAMOND BLOCKS rounded to the hundreths place
	that each of your friends find per mine.

	THIS MUST BE DONE IN ONE LINE

	HINT: There are nine diamonds in each diamond block.

	Args:
		num_diamonds (np.array)
		num_mines (np.array)

	Returns:
		np.array
		
	>>> num_diamonds = np.array([150,200,187,196])
	>>> num_mines = np.array([2,3,3,6])

	>>>  miner_ranker(num_diamonds, num_mines)
	array([8.33, 7.41, 6.93, 3.63])

	"""
	return np.round(np.array((num_diamonds / 9) / num_mines),decimals=2)

def broke_trade(emeralds, villager_costs):
	'''
	QUESTION 03
	
	You are trading with a villager, who offers multiple items for a specific number of emeralds. However, the villager is feeling
	nice, and giving you a discount based off the first digit of the number (e.g. for cost 25, you get a discount of 2 emeralds).
	After the discount, there is a 8.9% tax applied. You want to trade for the second most expensive item you can afford after the 
	tax and discount are applied, but return the pre-discount, pre-tax cost of the item you will purchase.

	THIS MUST BE DONE IN ONE LINE.

	Args:
		emeralds (int)
		villager_costs (np.array)

	Return:
		int64

	>>> emeralds = 25
	>>> villager_costs = np.array([10, 20, 15, 25, 30])

	>>> pprint(broke_trade(emeralds, villager_costs))
	15
	'''
	return np.sort(villager_costs[emeralds >= ((villager_costs - (villager_costs // 10))* 1.089)])[-2]

def wheat(wheat_quantities):
	"""
	QUESTION 04

	You have some villager friends with a lot of wheat, and you want to trade your five emeralds 
	with them so you can have some of their wheat. However, some of them will give you more wheat for
	five emeralds than others. You want to figure out what the largest amount of wheat you can get is, so 
	you can trade with that villager again. You are also wanting to cook a recipe which requires an even 
	amount of wheat, so you only want to look at the even values. You also do not want to trade with your 
	two least favorite villagers. The amounts from your two least favorite villagers will always be the first 
	two values in your array. Find the largest amount of wheat that one of your friends will give you, 
	excluding your two least favorite villagers and odd quantities. 

	THIS MUST BE DONE IN ONE LINE

	Args: 
		wheat_quantities (np.array)

	Returns:
		int

	>>> wheat_quantities = np.array([10, 2, 4, 9, 44, 28])
 
	>>> pprint(wheat(wheat_quantities))
	44

	"""
	return np.max(wheat_quantities[(wheat_quantities % 2 == 0)][2:])

def daily_wheat(wheat_data):
	"""
	QUESTION 05

	You have continued to collect data on how many pieces of wheat your villager friends will give you for 
	five emeralds. You now have their names and the days of the week that the trade was made! You want to see
	how many pieces of wheat each farmer gives you on average. However, you hate trading on weekends, so you
	do not want data from the weekend included. Return an array with the villager's name and the average
	amount of wheat they give you on weekdays. Round your averages to one decimal place.

	THIS MUST BE DONE IN ONE LINE

	Args:
		wheat_data (np.array)

	Returns:
		np.array
  
	>>> wheat_data = np.array([["Name","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], 
 							["Farmer 1", 23, 4, 1, 6, 9, 5, 2], ["Farmer 2", 6, 7, 2, 3, 14, 4, 12], ["Farmer 3", 14, 8, 17, 4, 5, 21, 3]])

	>>> pprint(daily_wheat(wheat_data))
	array([['Farmer 1', 'Farmer 2', 'Farmer 3'],
       ['5.0', '6.0', '11.0']], dtype='<U32')

	"""
	return np.array([wheat_data[1:,0],np.round(np.mean(wheat_data[1:,2:7].astype(float),axis=1),1)])

def enderdragon_prep(friend1_minedata, friend2_minedata, friend3_minedata):
	"""
	QUESTION 06
 
	You and your friends went mining three times to get ready to fight the enderdragon. The data from each person's mine is 
	recorded in a 2D array in the form:
		[[number_diamonds_mine1, number_diamonds_mine2, number_diamonds_mine3], [number_iron_1, number_iron_2, number_iron_3]]
	You want to figure out, between the three of you, how many full sets of diamond armour and iron swords you can make.
	Return an array with the total number of full sets of diamond armour you can make and how many iron swords you can make 
	rounded to the nearest whole number.

	THIS MUST BE DONE IN ONE LINE
 
	Note: You need 24 diamonds for a set of diamond armor, and 2 iron for an iron sword

	Args:
		friend1_minedata (np.array)
		friend2_minedata (np.array)
		friend3_minedata (np.array)

	Returns:
		np.array

	>>> friend1_minedata = np.array([[30,25,42],[12,42,73]])
	>>> friend2_minedata = np.array([[35,26,58],[90,57,82]])
	>>> friend3_minedata = np.array([[39,16,45],[40,87,72]])

	>>>  enderdragon_prep(friend1_minedata, friend2_minedata, friend3_minedata)
	array([ 13, 277])

	"""
	return np.array([(((friend1_minedata[0].sum()+friend2_minedata[0].sum()+friend3_minedata[0].sum())/ 24)).astype(int),((friend1_minedata[1].sum()+friend2_minedata[1].sum()+friend3_minedata[1].sum())/2).astype(int)])
	
def enchantment_books(available_books):
	"""
	QUESTION 07
	
	You are analyzing trades from a Minecraft villager's monthly offers of various enchanted books. The villager offers 
	different enchanted books, each with a specific price and level of demand.
	The trade data is set up in array form as ['book_name', number of purchases, price in emeralds]
	Demand should be classified based on the following criteria:
		- "High Demand": if the number of purchases > 100 and the price > 30 emeralds.
		- "Moderate Demand": if the number of purchases is between 50 and 100 (inclusive) or the price is between 15 and 30 emeralds (inclusive).
		- "Low Demand" otherwise
	Return an array containing "High Demand", "Moderate Demand", or "Low Demand" for each enchanted book in the demand_data array.
	
	THE ORDER IN WHICH YOU BUILD THE CONDITIONS MATTER, PLEASE FOLLOW THE EXACT ORDER WE GIVE YOU

	THIS MUST BE DONE IN ONE LINE.

	Args:
		available_books (np.array)

	Return:
		np.array

	>>> available_books = np.array([
		['Sharpness V', 150, 35],
		['Protection IV', 80, 20],
		['Mending', 120, 50],
		['Efficiency V', 60, 25],
		['Infinity', 30, 40],
		['Unbreaking III', 75, 10],
		['Thorns III', 45, 15]
	])

	>>> pprint(enchantment_books(available_books))
	array(['High Demand', 'Moderate Demand', 'High Demand', 'Moderate Demand', 'Low Demand', 
		   'Moderate Demand', 'Moderate Demand'], dtype = '<U15')
	
	"""
	return np.where((available_books[0:,1].astype(int) > 100) & (available_books[0:,2].astype(int) > 30),"High Demand",np.where(((available_books[0:,1].astype(int) >= 50) & (available_books[0:,1].astype(int) <=100)) | ((available_books[0:,2].astype(int) >= 15) & (available_books[0:,2].astype(int) <=30 )),"Moderate Demand","Low Demand"))

def find_village(coords):
	"""
	QUESTION 08

	You're searching for another village, but you've already checked out all the locations around your home!
	Now you want to go hunting elsewhere, and you've figured out the best x	and z coordinates for your next
	search. Using the random module (not np.random), generate a random z coordinate between -2000 and 2000 to start
	your search. Replace the np.nan values in your coords list with the new z value.

	Note: The new z value, an integer, will be the same for all coordinate locations.

	Args:
		coords (np.array)
	Returns:
		np.array

	>>>  coords = np.array([[1721, np.nan], [3144, np.nan], [1194, np.nan], [1620, np.nan], [1008, np.nan]])

	>>> pprint(find_village(coords)))
	array[[ 1721., -1450.]
 	 	  [ 3144., -1450.]
 	 	  [ 1194., -1450.]
 	 	  [ 1620., -1450.]
 	 	  [ 1008., -1450.]]

	"""
	#DO NOT REMOVE, BEGIN YOUR CODE AFTER THIS LINE#
	random.seed(1)
	##############

	z = random.randint(-2000,2000)
	coords[0:,1] = z
	return coords

if __name__ == "__main__":
	print("Question01")
	pprint(window_counter(4, 50))
	print("__________")
	
	print("Question02")
	pprint(miner_ranker(np.array([150,200,187,196]),np.array([2,3,3,6])))
	print("__________")

	print("Question03")
	emeralds = 25
	villager_costs = np.array([10, 20, 15, 25, 30])
	pprint(broke_trade(emeralds, villager_costs))
	print("__________")
	
	print("Question04")
	print(wheat(np.array([10, 2, 4, 9, 44, 28])))
	print(wheat(np.array([34, 2, 8, 5, 9, 10, 3])))
	print("__________")

	print("Question05")
	pprint(daily_wheat(np.array([["Name","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], ["Farmer 1", 23, 4, 1, 6, 9, 5, 2], ["Farmer 2", 6, 7, 2, 3, 14, 4, 12], ["Farmer 3", 14, 8, 17, 4, 5, 21, 3]])))
	pprint(daily_wheat(np.array([["Name","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], ["Farmer 1", 2, 13, 3, 5, 7, 4, 1], ["Farmer 2", 3, 5, 9, 12, 18, 23, 7], ["Farmer 3", 7, 4, 13, 2, 5, 0, 1]])))
	print("__________")
	
	print("Question06")
	pprint(enderdragon_prep(np.array([[30,25,42],[12,42,73]]), np.array([[35,26,58],[90,57,82]]), np.array([[39,16,45],[40,87,72]])))
	print("__________")
		
	print("Question07")
	available_books  = np.array([
	    ['Sharpness V', 150, 35],
	    ['Protection IV', 80, 20],
	    ['Mending', 120, 50],
	    ['Efficiency V', 60, 25],
	    ['Infinity', 30, 40],
	    ['Unbreaking III', 75, 10],
	    ['Thorns III', 45, 15]
	])
	pprint(enchantment_books(available_books))
	print("__________")
	
	print("Question08")
	coords = np.array([[1721, np.nan], [3144, np.nan], [1194, np.nan], [1620, np.nan], [1008, np.nan]])
	pprint(find_village(coords))
	print("__________")