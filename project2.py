from graphics import *

class Button:
    """A button that can be clicked."""
    def __init__(self, win, center, width, height, label):
        """Create a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit')"""

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('light blue')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)

    def clicked(self, p):
        """Return True if button active and p is inside"""
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

class RecipesWindow:
    def __init__(self, main_win):
        self.win = GraphWin("Recipes", 200, 600)
        self.text = Text(Point(100, 50), "Recipes Window")
        self.text.draw(self.win)
        self.breakfast_button = Button(self.win, Point(100, 150), 80, 20, "Breakfast")
        self.lunch_button = Button(self.win, Point(100, 250), 80, 20, "Lunch")
        self.dinner_button = Button(self.win, Point(100, 350), 80, 20, "Dinner")
        self.back_button = Button(self.win, Point(100, 500), 40, 20, "Back")

    def run(self):
        while True:
            p = self.win.getMouse()
            if p is None:
                break
            elif self.back_button.clicked(p):
                self.win.close()
                return
            elif self.breakfast_button.clicked(p):
                breakfastWindow(self.win)
            elif self.lunch_button.clicked(p):
                lunchWindow(self.win)
            elif self.dinner_button.clicked(p):
                dinnerWindow(self.win)
        self.win.close()

def open_recipes_window(main_win):
    """Open a new window for the recipes."""
    recipes_window = RecipesWindow(main_win)
    recipes_window.run()

class OpenRecipes:
    def __init__(self, main_win):
        win = GraphWin("Breakfast Recipes", 200, 600)
        text = Text(Point(100, 50), "Breakfast Recipes")
        text.draw(win)
        pancake_button = Button(win, Point(100, 150), 80, 20, "Pancakes")
        burrito_button = Button(win, Point(100, 250), 130, 20, "Breakfast Burritos")
        back_button = Button(win, Point(100, 500), 40, 20, "Back")

def breakfastWindow(main_win):
    """Open a new window for breakfast themed recipes."""
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
        elif pancake_button.clicked(p):
            with open('Pancakes.txt', 'r') as f:
                recipe = f.read()
            recipe_window = GraphWin("Pancake Recipe", 850, 600)
            recipe_text = Text(Point(425, 50), "Pancake Recipe")
            recipe_text.draw(recipe_window)
            recipe_display = Text(Point(425, 300), recipe)
            recipe_display.draw(recipe_window)
            back_button_recipe = Button(recipe_window, Point(425, 550), 40, 20, "Back")
            while True:
                p = recipe_window.getMouse()
                if p is None:
                    break
                elif back_button_recipe.clicked(p):
                    recipe_window.close()
                    break
            recipe_window.close()
        elif burrito_button.clicked(p):
            with open('BB.txt', 'r') as f:
                recipe = f.read()
            recipe_window = GraphWin("Breakfast Burrito Recipe", 1100, 600)
            recipe_text = Text(Point(550, 50), "Breakfast Burrito Recipe")
            recipe_text.draw(recipe_window)
            recipe_display = Text(Point(550, 300), recipe)
            recipe_display.draw(recipe_window)
            back_button_recipe = Button(recipe_window, Point(550, 550), 40, 20, "Back")
            while True:
                p = recipe_window.getMouse()
                if p is None:
                    break
                elif back_button_recipe.clicked(p):
                    recipe_window.close()
                    break
            recipe_window.close()
    win.close()

def lunchWindow(main_win):
    """Open a new window for lunch themed recipes."""
    win = GraphWin("Lunch Recipes", 200, 600)
    text = Text(Point(100, 50), "Lunch Recipes")
    text.draw(win)
    GCS_button = Button(win, Point(100, 150), 155, 20, "Grilled Chicken Salad")
    GSW_button = Button(win, Point(100, 250), 135, 20, "Greek Salad Wrap")
    back_button = Button(win, Point(100, 500), 40, 20, "Back")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
        elif GCS_button.clicked(p):
            with open('GCS.txt', 'r') as f:
                recipe = f.read()
            recipe_window = GraphWin("Grilled Chicken Salad Recipe", 1100, 950)
            recipe_text = Text(Point(475, 25), "Grilled Chicken Salad Recipe")
            recipe_text.draw(recipe_window)
            recipe_display = Text(Point(475, 300), recipe)
            recipe_display.draw(recipe_window)
            back_button_recipe = Button(recipe_window, Point(475, 625), 40, 20, "Back")
            while True:
                p = recipe_window.getMouse()
                if p is None:
                    break
                elif back_button_recipe.clicked(p):
                    recipe_window.close()
                    break
            recipe_window.close()
        elif GSW_button.clicked(p):
            with open('GSW.txt', 'r') as f:
                recipe = f.read()
            recipe_window = GraphWin("Greek Salad Wrap Recipe", 1100, 600)
            recipe_text = Text(Point(550, 50), "Greek Salad Wrap Recipe")
            recipe_text.draw(recipe_window)
            recipe_display = Text(Point(550, 300), recipe)
            recipe_display.draw(recipe_window)
            back_button_recipe = Button(recipe_window, Point(550, 550), 40, 20, "Back")
            while True:
                p = recipe_window.getMouse()
                if p is None:
                    break
                elif back_button_recipe.clicked(p):
                    recipe_window.close()
                    break
            recipe_window.close()
    win.close()

def dinnerWindow(main_win):
    """Open a new window for dinner themed recipes."""
    win = GraphWin("Dinner Recipes", 250, 600)
    text = Text(Point(125, 50), "Dinner Recipes")
    text.draw(win)
    SMB_button = Button(win, Point(125, 150), 175, 20, "Spaghetti and Meatballs")
    BSWA_button = Button(win, Point(125, 250), 225, 20, "Baked Salmon with Asparagus")
    back_button = Button(win, Point(125, 500), 40, 20, "Back")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
        elif SMB_button.clicked(p):
            with open('SMB.txt', 'r') as f:
                recipe = f.read()
            recipe_window = GraphWin("Spaghetti and Meatballs Recipe", 1000, 950)
            recipe_text = Text(Point(455, 25), "Spaghetti and Meatballs Recipe")
            recipe_text.draw(recipe_window)
            recipe_display = Text(Point(455, 300), recipe)
            recipe_display.draw(recipe_window)
            back_button_recipe = Button(recipe_window, Point(455, 615), 40, 20, "Back")
            while True:
                p = recipe_window.getMouse()
                if p is None:
                    break
                elif back_button_recipe.clicked(p):
                    recipe_window.close()
                    break
            recipe_window.close()
        elif BSWA_button.clicked(p):
            with open('BSWA.txt', 'r') as f:
                recipe = f.read()
            recipe_window = GraphWin("Baked Salmon with Asparagus Recipe", 1100, 600)
            recipe_text = Text(Point(550, 50), "Baked Salmon with Asparagus Recipe")
            recipe_text.draw(recipe_window)
            recipe_display = Text(Point(550, 300), recipe)
            recipe_display.draw(recipe_window)
            back_button_recipe = Button(recipe_window, Point(550, 575), 40, 20, "Back")
            while True:
                p = recipe_window.getMouse()
                if p is None:
                    break
                elif back_button_recipe.clicked(p):
                    recipe_window.close()
                    break
            recipe_window.close()
    win.close()

class addButton:
    def __init__(main_win):
        win = GraphWin("Recipes", 200, 600)
        text = Text(Point(100, 50), "Recipes Window")
        text.draw(win)
        breakfast_button = Button(win, Point(100, 150), 80, 20, "Breakfast")
        lunch_button = Button(win, Point(100, 250), 80, 20, "Lunch")
        dinner_button = Button(win, Point(100, 350), 80, 20, "Dinner")
        back_button = Button(win, Point(100, 500), 40, 20, "Back")

def addWindow(main_win):
    """Open a new window for adding recipes."""
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
        elif breakfast_button.clicked(p):
            print("Breakfast recipes")
        elif lunch_button.clicked(p):
            print("Lunch recipes")
        elif dinner_button.clicked(p):
            print("Dinner recipes")
    win.close()

def main():
    # create the main window
    win = GraphWin("Main Window", 300, 300)

    # title
    title = Text(Point(150, 50), "Recipe Book")
    title.draw(win)

    # create the buttons
    quit_button = Button(win, Point(50, 150), 40, 20, "Quit")
    recipes_button = Button(win, Point(150, 150), 60, 20, "Recipes")
    add_button = Button(win, Point(250, 150), 40, 20, "Add")

    # wait for user to click a button or close the window
    while True:
        p = win.getMouse()
        if quit_button.clicked(p):
            win.close()
            break
        elif recipes_button.clicked(p):
            open_recipes_window(win)
        elif add_button.clicked(p):
            addWindow(win)


if __name__ == '__main__':
    main()
