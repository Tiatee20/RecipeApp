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
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)

    def clicked(self, p):
        """Return True if button active and p is inside"""
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

def open_recipes_window(main_win):
    """Open a new window for the recipes."""
    win = GraphWin("Recipes", 200, 600)
    text = Text(Point(100, 50), "Recipes Window")
    text.draw(win)
    breakfast_button = Button(win, Point(100, 150), 80, 20, "Breakfast")
    lunch_button = Button(win, Point(100, 250), 80, 20, "Lunch")
    dinner_button = Button(win, Point(100, 350), 80, 20, "Dinner")
    back_button = Button(win, Point(100, 500), 40, 20, "Back")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
        elif breakfast_button.clicked(p):
            open_breakfast_window(win)
        elif lunch_button.clicked(p):
            open_lunch_window(win)
        elif dinner_button.clicked(p):
            open_dinner_window(win)
    win.close()


def open_breakfast_window(main_win):
    """Open a new window for breakfast themed recipes."""
    win = GraphWin("Breakfast Recipes", 200, 600)
    text = Text(Point(100, 50), "Breakfast Recipes")
    text.draw(win)
    pancake_button = Button(win, Point(100, 150), 80, 20, "Pancakes")
    burrito_button = Button(win, Point(100, 250), 130, 20, "Breakfast Burritos")
    back_button = Button(win, Point(100, 500), 40, 20, "Back")
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

def open_lunch_window(main_win):
    """Open a new window for lunch themed recipes."""
    win = GraphWin("Lunch Recipes", 200, 600)
    text = Text(Point(100, 50), "Lunch Recipes")
    text.draw(win)
    pancake_button = Button(win, Point(100, 150), 155, 20, "Grilled Chicken Salad")
    burrito_button = Button(win, Point(100, 250), 135, 20, "Greek Salad Wrap")
    back_button = Button(win, Point(100, 500), 40, 20, "Back")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
        elif pancake_button.clicked(p):
            print("Pancake recipe")
        elif burrito_button.clicked(p):
            print("Breakfast burrito recipe")
    win.close()

def open_dinner_window(main_win):
    """Open a new window for dinner themed recipes."""
    win = GraphWin("Dinner Recipes", 250, 600)
    text = Text(Point(125, 50), "Dinner Recipes")
    text.draw(win)
    pancake_button = Button(win, Point(125, 150), 175, 20, "Spaghetti and Meatballs")
    burrito_button = Button(win, Point(125, 250), 225, 20, "Baked Salmon with Asparagus")
    back_button = Button(win, Point(125, 500), 40, 20, "Back")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
        elif pancake_button.clicked(p):
            print("Pancake recipe")
        elif burrito_button.clicked(p):
            print("Breakfast burrito recipe")
    win.close()

def open_add_window(main_win):
    """Open a new window for adding recipes."""
    win = GraphWin("Recipes", 200, 600)
    text = Text(Point(100, 50), "Recipes Window")
    text.draw(win)
    breakfast_button = Button(win, Point(100, 150), 80, 20, "Breakfast")
    lunch_button = Button(win, Point(100, 250), 80, 20, "Lunch")
    dinner_button = Button(win, Point(100, 350), 80, 20, "Dinner")
    back_button = Button(win, Point(100, 500), 40, 20, "Back")
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
            open_add_window(win)


if __name__ == '__main__':
    main()
