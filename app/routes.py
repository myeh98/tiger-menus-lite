import requests
from app import app
from pprint import pprint
from bs4 import BeautifulSoup
from app.charter import charter
from app.colonial import colonial
from flask import render_template
from datetime import datetime, timedelta


@app.route('/hello')
def hello():
    return '<p>Hello World!</p>'


@app.route('/')
@app.route('/index')
def index():
    return meal(9, 13, 2017)


def getButler(m, d, y):
    """Get Butler menus for a specific date from the TigerMenus API

    :param int m: month
    :param int d: day
    :param int y: year

    :return: lunch and dinner lists for a specific day
    :rtype: tuple(list, list)
    """
    butlerLunch = []
    butlerDinner = []

    url = "https://tigermenus.herokuapp.com/api/{}/{}/{}".format(m, d, y)

    # STUDENT CODE BEGIN ( Ref < 10 lines)

    # STUDENT CODE END

    return butlerLunch, butlerDinner


def getColonial(dateString):
    """Get Colonial menus for a specific date from the colonial.py file

    :param str dateString: a string in a format like 2017-09-11

    :return: lunch and dinner lists for a specific day
    :rtype: tuple(list, list)
    """
    colonialLunch = []
    colonialDinner = []

    c = [item for item in colonial if item['date'] == dateString]

    # STUDENT CODE BEGIN (Ref < 20 lines)

    # STUDENT CODE END

    return colonialLunch, colonialDinner


def getCharter(dateString):
    """
    :param str dateString: a string in a format like 2017-09-11
    """
    charterLunch = ['Lunch', '-- Entrees --']
    charterDinner = ['Dinner', '-- Entrees --']

    charterLunch += charter['lunch'][dateString]
    charterDinner += charter['dinner'][dateString]

    return charterLunch, charterDinner


@app.route('/<int:m>/<int:d>/<int:y>')
def meal(m, d, y):
    date = datetime(y, m, d)
    yesterday = date - timedelta(days=1)
    tomorrow = date + timedelta(days=1)

    dateString = datetime(y, m, d).strftime("%Y-%m-%d")
    yString = yesterday.strftime("%m/%d/%Y")
    tString = tomorrow.strftime("%m/%d/%Y")

    butlerLunch, butlerDinner = getButler(m, d, y)
    colonialLunch, colonialDinner = getColonial(dateString)
    charterLunch, charterDinner = getCharter(dateString)

    lists = [
        ['Colonial', colonialLunch],
        ['Charter', charterLunch],
        ['Butler', butlerLunch],
        ['Colonial', colonialDinner],
        ['Charter', charterDinner],
        ['Butler', butlerDinner]
    ]

    return render_template('index.html', lists=lists, dateString=dateString,
                           yString=yString, tString=tString)
