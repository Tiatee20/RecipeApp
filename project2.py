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
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
    win.close()

def open_add_window(main_win):
    """Open a new window for adding recipes."""
    win = GraphWin("Add Recipe", 200, 200)
    text = Text(Point(100, 100), "Add Recipe Window")
    text.draw(win)
    back_button = Button(win, Point(100, 150), 40, 20, "Back")
    while True:
        p = win.getMouse()
        if p is None:
            break
        elif back_button.clicked(p):
            win.close()
            return
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
