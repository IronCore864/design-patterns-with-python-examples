class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        print(f'\tDrawn at point {x}, {y} on canvas {canvas}')


class TreeFactory:
    tree_types = []

    @classmethod
    def get_tree_type(cls, name, color, texture):
        for t in cls.tree_types:
            if t.name == name and t.color == color and t.texture == texture:
                return t
        t = TreeType(name, color, texture)
        cls.tree_types.append(t)
        return t


class Tree(TreeType):
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def draw(self, canvas):
        print(
            f'Prepare to draw a tree, type: {self.type.name}, {self.type.color}, {self.type.texture}')
        self.type.draw(canvas, self.x, self.y)


class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, type)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)


if __name__ == '__main__':
    forest = Forest()
    forest.plant_tree(0, 0, 'A', 'green', 'smooth')
    forest.plant_tree(1, 1, 'A', 'green', 'smooth')
    forest.plant_tree(2, 2, 'A', 'green', 'smooth')

    forest.plant_tree(3, 3, 'B', 'red', 'not-so-smooth')
    forest.plant_tree(4, 4, 'B', 'red', 'not-so-smooth')

    forest.plant_tree(5, 5, 'C', 'yellow', 'definitely-not-smooth')
    forest.plant_tree(6, 6, 'C', 'yellow', 'definitely-not-smooth')
    forest.plant_tree(7, 7, 'C', 'yellow', 'definitely-not-smooth')

    forest.draw("Canvas 1")
