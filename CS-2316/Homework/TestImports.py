def test_imports():
    count = 0
    modulelist = []

# Test correct installation of requests

    try:
        import requests
        url = "http://cc.gatech.edu"
        r = requests.get(url)
        print("True - requests")
    except:
        count += 1
        modulelist.append("requests")
        print("False - requests not successfully imported")

# Test correct installation of pyqt5

    try:
        from PyQt5.QtWidgets import (
            QApplication,
            QWidget,
            QPushButton,
            QRadioButton,
            QHBoxLayout,
            QVBoxLayout,
            QLabel,
            QLineEdit,
            QListWidget
            )
        print("True - PyQt5")
    except:
        count += 1
        modulelist.append("PyQt5")
        print("False - PyQt5 not successfully imported")

# Test correct installation of beautifulsoup

    try:
        from bs4 import BeautifulSoup
        resp = requests.get("https://scrapethissite.com/pages/simple/")
        soup = BeautifulSoup(resp.text, "html.parser")
        print("True - BeautifulSoup")
    except:
        count += 1
        modulelist.append("BeautifulSoup")
        print("False - BeautifulSoup not successfully imported")

# Test correct installation of numpy

    try:
        import numpy as np
        a1 = np.array([[1,2,3],[4,5,6]])
        a2 = a1[0:2,1:3]
        a3 = a1[:,0]
        print("True - numpy")
    except:
        count += 1
        modulelist.append('numpy')
        print("False - numpy not successfully imported")

# Test correct installation of pandas

    try:
        import pandas as pd
        s1 = pd.Series([1,2,3],index = ["a","b","c"])
        s1 = s1.sort_values(ascending = False)
        df1 = pd.DataFrame(np.ones((3,4)), index=list('ABC'), columns=list('efgh'))
        print("True - pandas")
    except:
        count += 1
        modulelist.append('pandas')
        print("False - pandas not successfully imported")

# Test correct installation of pymysql

    try:
        import pymysql
        print("True - pymysql")
    except:
        count += 1
        modulelist.append('pymysql')
        print("False - pymysql not successfully imported")

# Test correct installation of matplotlib

    try:
        import matplotlib.pyplot as plt
        print("True - matplotlib")
    except:
        count += 1
        modulelist.append('matplotlib')
        print("False - matplotlib not successfully imported")

# Test correct installation of jupyter

    try:
        import jupyter
        print("True - jupyter")
    except:
        count += 1
        modulelist.append('jupyter')
        print("False - jupyter not successfully imported")

# Test correct installation of plotly

    try:
        import plotly.express as px
        a = np.arange(0,10,.25)
        b = np.sin(a)
        c = np.cos(a) + 1
        fig = px.scatter(x = a, y = [b, c])

        print("True - plotly")
    except:
        count += 1
        modulelist.append('plotly')
        print("False - plotly not successfully imported")

    if count == 0:
        print_string = "Processing complete - no further installations necessary"
    else:
        print_string = f"Processing complete - please install {count} further modules:\n#"

    print("#\n#\n#\n#\n#\n#\n#\n#")

    print(print_string)

    for i in modulelist:
        print(i)

    if count > 0:
        print("If you are having problems with your installations please see the TAs\nfor further assistance. Come to offic hours, post on ED Discussion board,\nor email a TA.\n#\n#\nNOTE: The closer it is to the due date of this assignment the busier the TAs \nwill be meaning there is a chance they will not be able to assist you.")

test_imports()

