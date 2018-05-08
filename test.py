from itertools import zip_longest
from app.routes import getButler, getColonial

dateString = "2017-09-13"


def compare(meal, correct, name, hall):
    if meal == correct:
        print("Correct " + hall + " " + name)
        return True
    else:
        print("Incorrect " + hall + " " + dateString + " " + name)
        print()
        print('{0:60}  {1}'.format("Reference:", "Yours:"))
        print()
        zl = zip_longest(correct, meal, fillvalue="")
        for i, j in zl:
            print('{0:60}  {1}'.format(i, j))
        print("-"*120)
        return False


# TEST BUTLER
butlerLunch, butlerDinner = getButler(9, 13, 2017)

correctButlerLunch = [
 'Lunch',
 '-- Main Entree --',
 'Roast Beef with Red Wine Demi-Glace',
 '-- Soups --',
 'Italian Wedding Soup',
 'Split Pea Soup',
 '-- Grill Special --',
 'Fish Taco Grill',
 '-- On the Side --',
 'Roasted Yukon Gold Potatoes',
 'Stewed Green Beans',
 '-- Action Station --',
 'Bean & Green Station with Dark Greens & Seeds',
 '-- Specialty Bars --',
 'Beef Burrito Bowl'
 ]

correctButlerDinner = [
 'Dinner',
 '-- Main Entree --',
 'Chicken Nuggets',
 'Cod Nuggets',
 '-- Vegetarian & Vegan Entree --',
 'Grilled Tofu',
 '-- Soups --',
 'Italian Wedding Soup',
 'Split Pea Soup',
 '-- On the Side --',
 'Au Gratin Potatoes',
 'Whole Baby Carrots',
 '-- Specialty Bars --',
 'Asian Noodle Soup Bar'
 ]

compare(butlerLunch, correctButlerLunch, "lunch", 'Butler')
compare(butlerDinner, correctButlerDinner, "dinner", "Butler")


# TEST COLONIAL
colonialLunch, colonialDinner = getColonial(dateString)

correctColonialLunch = [
 'Lunch',
 '-- Hot Line --',
 'Vegan Quinoa Bowls with corn, avocado, beans, pico de gallo.',
 'raviolis with caper-tomato/ Veggie Medley',
 'lemon-rosemary grilled chicken',
 'French fries/ sweet potato chips',
 'Lamb gyros / Falafel gyros',
 '-- On the Grill --',
 'lots of options made to order'
]

correctColonialDinner = [
 'Dinner',
 '-- Hot Line --',
 'Eggplant rollentini with ricotta',
 'Tortellini alfredo/ Veggie medley',
 'roasted rosemary potatoes/ Cauliflower rice',
 'Pesto crusted tilapia served with pomodoro',
 'Honey-balsamic grilled chicken',
 '-- On the Grill --',
 'ham and cheese sliders'
]

compare(colonialLunch, correctColonialLunch, 'lunch', 'Colonial')
compare(colonialDinner, correctColonialDinner, 'dinner', 'Colonial')
