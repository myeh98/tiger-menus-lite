from scrape import scrape
from datetime import datetime
from itertools import zip_longest


def compare(meal, correct, name, hall):
    if meal == correct:
        print("Correct " + hall + " " + name)
        return True
    else:
        for date, correctItems in correct.items():
            if meal[date] != correctItems:
                print("Incorrect " + hall + " " + date + " " + name)
                print()
                print('{0:60}  {1}'.format("Reference:", "Yours:"))
                print()
                zl = zip_longest(correctItems, meal[date], fillvalue="")
                for i, j in zl:
                    print('{0:60}  {1}'.format(i, j))
                print("-"*120)
        return False


def test_scrape(lunch, dinner):
    correctCharterLunch = {
     '2017-09-11': [],
     '2017-09-12': [],
     '2017-09-13': ['Soup du Jour',
                    'Gyros or Falafel on Pita Bread',
                    'French Fries',
                    "Chef's Choice of Hot Vegetables",
                    'GRILL SPECIAL: California Turkey Club',
                    'SPECIAL SALAD: Buffalo Chicken Salad',
                    'Blondies'],
     '2017-09-14': ['Soup du Jour',
                    'Tacos or Burritos (Beef, Chicken, Bean)',
                    'Roasted Sweet Plaintains, Refried Beans, Nachos',
                    "Chef's Choice of Hot Vegetables",
                    'GRILL SPECIAL: Fried Chicken Sand. with Kale',
                    'SPECIAL SALAD: Avocado Shrimp Salad',
                    'Assorted Cookies'],
     '2017-09-15': ['Soup du Jour',
                    'Gyros or Falafel on Pita Bread',
                    'French Fries',
                    "Chef's Choice of Hot Vegetables",
                    'CREPES #1: Strawberry-Banana & Nutella',
                    'CREPE # 2: Jam & Jarlsberg',
                    'SPECIAL SALAD: Seafood Salad',
                    'Assorted Ice Cream Bars'],
     '2017-09-16': ['Bacon, Pork Roll, Muffins, Scones, Bagels',
                    'Apple Turnovers, Fresh Cut Fruit, Smoked Salmon',
                    'Blueberry or Chocolate Chip Pancakes',
                    'Hash Brown Potatoes',
                    'OMELETTE: Broccoli, Tomato, Chive & Cheddar',
                    'BREAKFAST SPECIAL: Bacon, Egg & Cheese on a English Muffin',
                    'LUNCH SPECIAL: French Dipped Sandwich with Provolone'],
     '2017-09-17': ['Sausage, Ham, Muffins, Croissants',
                    'Danish, Bagels, Fresh Cut Fruit, Smoked Salmon',
                    'Cheese Blintzes with Warm Apple Compote',
                    'Tater Tots',
                    'OMELETTE: Broccoli and Boursin Cheese',
                    'BREAKFAST SPECIAL: "The Sally" Breakfast Sandwich',
                    'LUNCH SPECIAL: Crock of Santa Fe Green Chili Turkey Chili']}

    correctCharterDinner = {
     '2017-09-11': [],
     '2017-09-12': ['Grilled Santa Maria Beef Tri Tip Sandwich & Chipotle Onions',
                    'Grilled Hot Dogs with Kraut',
                    'Grilled Gardenburgers',
                    'New Jersey Fresh Corn on the Cob',
                    'Stuffed Shells with Vodka Tomato Sauce',
                    'Plum Tomato, Basil & Fresh Mozzarella Salad',
                    'Chilled Watermelon',
                    'Ice Cream Bar'],
     '2017-09-13': ["General Tso's Chicken or Tofu",
                    'Indonesian Mie Goreng (Stir Fried Rice Noodles)',
                    'Egg Rolls',
                    'Scallion Pancakes',
                    'Jasmine Rice',
                    'Fresh Pineapple Spears',
                    'Fortune Cookies',
                    'Sorbet'],
     '2017-09-14': ['Caramelized Onion & Cheese Stuffed Giant Burger',
                    'with Smoked Bacon & Chipotle Ketchup',
                    'Roasted Salmon with Chilled Tarragon Sauce',
                    'Roasted Portabello & Tofu with Roasted Red Pepper Sauce',
                    'Pub Night Desserts'],
     '2017-09-15': ["Chef Tom's Gourmet Pizza",
                    'Boneless Wings',
                    'Sweet Potato Fries',
                    'Giant Cookies'],
     '2017-09-16': ['Pasta Bar, Soup Du Jour',
                    'Chicken Dijon, Mustard Cream Sauce',
                    'VEG: Cornmeal Crusted Tofu, Cilantro Sauce',
                    'Wild Rice Blend',
                    'Baby Carrots and Green Beans',
                    'Dinner Rolls',
                    'Assorted Layer Cakes'],
     '2017-09-17': []}

    compare(lunch, correctCharterLunch, 'lunch', 'Charter')
    compare(dinner, correctCharterDinner, 'dinner', 'Charter')


if __name__ == '__main__':
    date = datetime(2017, 9, 11)
    name = "charter/2017-09-11.html"
    lunch, dinner = scrape(name, date)
    test_scrape(lunch, dinner)
