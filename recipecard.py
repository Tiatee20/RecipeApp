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

if __name__ == '__main__':
    recipe = RecipeCard('BB.txt')
    print(recipe.name)
    print(recipe.meal)
    print(recipe.prep)
    print(recipe.cats)
    print(recipe.ingredients)
    print(recipe.instructions)
