import re
import sys
from pprint import pprint
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def scrape(name, date):
    """Scrape a charter HTML webpage

    :param str name: a string containing a webpage filename
    :param datetime date: a datetime object representing the week's Monday

    :return: lunch and dinner dictionaries mapping strings in the form
             "2017-09-11" to lists of food item strings
    :rtype: tuple(dict, dict)
    """
    lunch = {}
    dinner = {}

    for i in range(7):
        temp = date + timedelta(days=i)
        d = temp.strftime("%Y-%m-%d")
        lunch[d] = []
        dinner[d] = []

    # STUDENT CODE BEGIN (Ref < 30 lines)
    # with open(name) as html:
    
    # STUDENT CODE END

    return lunch, dinner


if __name__ == '__main__':
    start = datetime(2017, 9, 11)
    end = datetime(2018, 1, 22) + timedelta(days=7)

    date = start

    charterLunch = {}
    charterDinner = {}

    while date < end:
        name = "charter/" + date.strftime("%Y-%m-%d") + ".html"
        lunch, dinner = scrape(name, date)
        charterLunch.update(lunch)
        charterDinner.update(dinner)

        date += timedelta(days=7)

    print("charter = ", end="")
    pprint({'lunch': charterLunch, 'dinner': charterDinner})
