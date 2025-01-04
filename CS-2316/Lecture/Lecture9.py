import requests
from bs4 import BeautifulSoup
from pprint import pprint


resp = requests.get ("https://scrapethissite.com/pages/simple/")
soup = BeautifulSoup(resp.text, "html.parser")

# Lecture 9 Example 1

"""

country_tags = soup.find_all("h3")
# print(country_tags[0])
for country_tag in country_tags:
	print(country_tag.text.strip())

"""

# Lecture 9 Example 2

"""

countries = soup.find_all("div", {"class":"col-md-4 country"})
country_capital_dict = {}
for i in countries:
	country_capital_dict[i.find("h3").text.strip()] = i.find("span").text.strip()
print(country_capital_dict)

"""

# Lecture 9 Example 3

"""

countries = soup.find_all("div" , {"class":"col-md-4 country"})
country_flag_dict = {}
for country in countries:
	country_flag_dict[country.find("h3").text.strip()] = country.find("i")["class"][0] + ".jpg"
pprint(country_flag_dict)

"""

# Lecture 9 Coding Exercise

pull = requests.get("https://en.wikipedia.org/wiki/List_of_James_Bond_films")
parse = BeautifulSoup(pull.text, "html.parser")

tables = parse.find("table")
rows = tables.find_all("tr")
for row in rows[2:]:
	name = row.find("th").text.strip()
	pprint(name)

