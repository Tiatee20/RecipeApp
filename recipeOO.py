from graphics import *
from project2 import Button

class MainWin:
    def __init__(self):
        self.win = win = GraphWin('RecipeApp', 200, 600)
        self.closeButton = Button(win, Point(100, 500), 100, 30, 'Close')
        self.newButton = Button(win, Point(100, 450), 100, 30, 'Add Recipe')
        self.breakfastButton = Button(win, Point(100, 250), 100, 30, "Breakfast Recipes")
        self.lunchButton = Button(win, Point(100, 300), 100, 30, 'Lunch Recipes')
        self.dinnerButton = Button(win, Point(100, 350), 100, 30, "Dinner Recipes")

    def run(self):
        p = Point(0, 0)
        while not self.closeButton.clicked(p):
            p = self.win.getMouse()
            if self.lunchButton.clicked(p):
                lunchWin = SubWin('Lunch')
                lunchWin.run()
            elif self.breakfastButton.clicked(p):
                breakfastWin = SubWin('Breakfast')
                breakfastWin.run()
            elif self.dinnerButton.clicked(p):
                dinnerWin = SubWin('Dinner')
                dinnerWin.run()

class SubWin:
    def __init__(self, menu):
        self.name = menu
        self.win = GraphWin('{} Items'.format(menu), 200, 400)
        self.closeButton = Button(self.win, Point(100, 350), 100, 30, 'Close')

    def run(self):
        p = self.win.getMouse()
        while not self.closeButton.clicked(p):
            p = self.win.getMouse()
        self.win.close()

class Recipes:
    def __init__(self):
        self.win = win = GraphWin('RecipeApp', 200, 600)
        self.closeButton = Button(win, Point(100, 500), 100, 30, 'Close')
        self.newButton = Button(win, Point(100, 450), 100, 30, 'Add Recipe')
        self.pancakeButton = Button(win, Point(100, 150), 80, 20, "Pancake Recipe")
        self.burritoButton = Button(win, Point(100, 250), 130, 20, "Breakfast Burrito Recipe")

    def run(self):
        p = Point(0, 0)
        while not self.closeButton.clicked(p):
            p = self.win.getMouse()
            if self.pancakeButton.clicked(p):
                pancakeWin = SubWin2('Pancakes')
                pancakeWin.run()
                open.self.win()
            elif self.burritoButton.clicked(p):
                burritoWin = SubWin2('Breakfast Burritos')
                burritoWin.run()

class SubWin2:
    def __init__(self, menu):
        self.name = menu
        self.win = GraphWin('{} Items'.format(menu), 200, 400)
        self.closeButton = Button(self.win, Point(100, 350), 100, 30, 'Close')

    def run(self):
        p = self.win.getMouse()
        while not self.closeButton.clicked(p):
            p = self.win.getMouse()
        self.win.close()

class RecipeCard:
    def __init__(self, filename):
        file = open(filename, 'r')
        self.file = filename
        self.name = file.readline().replace('\n','')
        self.meal = file.readline().replace('\n','')
        self.prep = file.readline().replace('\n','')
        self.cats = file.readline().replace('\n','').split(',')
        file.readline()
        self.ingredients = []
        self.instructions = []
        while True:
            line = file.readline()
            if line == 'instructions\n':
                break
            self.ingredients.append(line.replace('\n',''))
        while True:
            line = file.readline()
            print(line)
            if (line == '') | (line == '\n'):
                break
            self.instructions.append(line.replace('\n',''))



        file.close()



class OpenRecipes:
    def __init__(self):
        while True:
            p = win.getMouse()
            if p is None:
                break
            elif closeButton.clicked(p):
                win.close()
                return
            elif pancakeButton.clicked(p):
                with open('Pancakes.txt', 'r') as f:
                    recipe = f.read()
            elif burritoButton.clicked(p):
                with open('BB.txt', 'r') as f:
                    recipe = f.read()


if __name__ == '__main__':
    app = MainWin()
    app.run()
    #recipe = RecipeCard('BB.txt') #breakfast burrito recipe - BREAKFAST
    #recipe = RecipeCard('BSWA.txt') #baked salmon w/asparagus recipe - DINNER
    #recipe = RecipeCard('GCS.txt') #grilled chicken salad recipe - LUNCH
    #recipe = RecipeCard('GSW.txt') #greek salad wrap recipe - LUNCH
    #recipe = RecipeCard('Pancakes.txt') #pancake recipe - BREAKFAST
    #recipe = RecipeCard('SMB.txt') #spaghetti and meatballs recipe - DINNER
    #print(recipe.name)
    #print(recipe.meal)
    #print(recipe.prep)
    #print(recipe.cats)
    #print(recipe.ingredients)
    #print(recipe.instructions)

