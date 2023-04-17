from graphics import *
from recipeapp import Button

class MainWin:

    def __init__(self):
        self.win = win = GraphWin('RecipeApp', 200, 600)
        self.closeButton = Button(win, Point(100, 500), 100, 30, 'Close')
        self.newButton = Button(win, Point(100, 450), 100, 30, 'Add Recipe')
        self.lunchButton = Button(win, Point(100, 350), 100, 30, 'Lunch Recipes')

    def run(self):
        p = Point(0, 0)
        while not self.closeButton.clicked(p):
            p = self.win.getMouse()
            if self.lunchButton.clicked(p):
                lunchWin = SubWin('Lunch')
                lunchWin.run()

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



if __name__ == '__main__':
    app = MainWin()
    app.run()
