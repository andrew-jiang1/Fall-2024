print([city[0] if "y" in city[0] else city[1] for city in {"Italy" : 10000, "Iceland" : 1160, "Vermont" : 200, "Greece" : 7000,"Germany" :2008}.items() if city[1] > 2000])
