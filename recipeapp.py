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
    win = GraphWin("Recipes", 600, 600)
    text = Text(Point(100, 100), "Recipes Window")
    text.draw(win)
    back_button = Button(win, Point(100, 150), 40, 20, "Back")
    breakfast_button = Button(win, Point(290, 200), 55, 50, "Breakfast")
    lunch_button = Button(win, Point(290, 290), 55, 60, "Lunch")
    dinner_button = Button(win, Point(290, 400), 55, 60, "Dinner")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
        elif breakfast_button.clicked(p):
            open_add_window1(win)
        elif lunch_button.clicked(p):
            open_add_window2(win)
        elif dinner_button.clicked(p):
            open_add_window3(win)
    win.close()

def open_add_window1(main_win):
    """Open a new window for breakfast recipes."""
    win = GraphWin("Add Breakfast Recipe", 400, 400)
    text = Text(Point(100, 100), "Add Breakfast Recipes")
    text.draw(win)
    back_button = Button(win, Point(100, 150), 40, 20, "Back")
    pancake_button = Button(win, Point(250, 300), 50, 60, "Pancake")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
        elif pancake_button.clicked(p):
            open_add_window1(win)

def open_add_window2(main_win):
    """Open a new window for lunch recipes."""
    win = GraphWin("Add Lunch Recipe", 400, 400)
    text = Text(Point(100, 100), "Add Lunch Recipes")
    text.draw(win)
    back_button = Button(win, Point(100, 150), 40, 20, "Back")
    sandwhich_button = Button(win, Point(250, 300), 50, 60, "Sandwhich")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
        elif sandwhich_button.clicked(p):
            open_add_window2(win)

def open_add_window3(main_win):
    """Open a new window for dinner recipes."""
    win = GraphWin("Add Dinner Recipe", 400, 400)
    text = Text(Point(100, 100), "Add Dinner Recipes")
    text.draw(win)
    back_button = Button(win, Point(100, 150), 40, 20, "Back")
    spaghetti_button = Button(win, Point(250, 300), 50, 60, "Spaghetti")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
        elif spaghetti_button.clicked(p):
            open_add_window3(win)

def open_breakfast_recipes(main, win):
    """Opens a new window for the breakfast recipes."""
    win = GraphWin("Breakfast Recipes", 600, 600)
    text = Text(Point(100, 100), "Breakfast Recipes Window")
    text.draw(win)
    back_button = Button(win, Point(100, 150), 40, 20, "Back")
    breakfast_button = Button(win, Point(260, 230), 55, 50, "Breakfast")
    lunch_button = Button(win, Point(290, 350), 55, 60, "Lunch")
    dinner_button = Button(win, Point(300, 400), 65, 80, "Dinner")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
        elif breakfast_button.clicked(p):
            open_add_window1(win)
    win.close()

def open_lunch_recipes(main, win):
    """Opens a window for the lunch recipes"""
    win = GraphWin("Lunch Recipes", 600, 600)
    text = Text(Point(100, 100), "Lunch Recipes Window")
    text.draw(win)
    back_button = Button(win, Point(100, 150), 40, 20, "Back")
    breakfast_button = Button(win, Point(260, 230), 55, 50, "Breakfast")
    lunch_button = Button(win, Point(290, 350), 55, 60, "Lunch")
    dinner_button = Button(win, Point(300, 400), 65, 80, "Dinner")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
        elif lunch_button.clicked(p):
            open_add_window2(win)
    win.close()

def open_dinner_recipes(main, win):
    """Opens a window for the dinner recipes"""
    win = GraphWin("Dinner Recipes", 600, 600)
    text = Text(Point(100, 100), "Dinner Recipes Window")
    text.draw(win)
    back_button = Button(win, Point(100, 150), 40, 20, "Back")
    breakfast_button = Button(win, Point(260, 230), 55, 50, "Breakfast")
    lunch_button = Button(win, Point(290, 350), 55, 60, "Lunch")
    dinner_button = Button(win, Point(300, 400), 65, 80, "Dinner")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
        elif dinner_button.clicked(p):
            open_add_window3(win)
    win.close()


def main():
    # create the main window
    win = GraphWin("My Window", 200, 200)

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
