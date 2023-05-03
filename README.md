# RecipeApp
A recipe app used to find food inspiration

# To-Do List
1. Create two recipes for each category 
2. Create the Add button
3. Create the app layout
4. Create recipes button
5. List title, ingredients, and directions for each recipe once a window is opened
6. Make quit button
7. Create categories breakfast, lunch, and dinner
8. Make txt file for each recipe
9. Make back button
10. Create a separate window for each category
11. Add images if possible

# Pseudocode
from graphics import *

class Button:
    """A button that can be clicked."""
    def __init__(self, win, center, width, height, label):
        """Create a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit')"""
#Create button 

class RecipesWindow:
    def __init__(self, main_win):
    #List all the recipe buttons and GraphWin
    
    def run(self):
      #Makes the buttons work once clicked
      
def open_recipes_window(main_win):
    """Open a new window for the recipes."""
    recipes_window = RecipesWindow(main_win)
    recipes_window.run()
    
 class OpenRecipes:
    def __init__(self, main_win):
    #list all the recipes 

def breakfastWindow(main_win):
    """Open a new window for breakfast themed recipes."""
    #Opens the breakfast recipes when run
    
 def lunchWindow(main_win):
    """Open a new window for lunch themed recipes."""
    #Opens the lunch recipes when run
    
def dinnerWindow(main_win):
  """Open a new window for dinner themed recipes."""
    #Opens the dinner recipes when run
   
class addButton:
    def __init__(main_win):
    #Makes the add button
    
def addWindow(main_win):
    """Open a new window for adding recipes."""
  
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
