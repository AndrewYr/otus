import random
from datetime import datetime


class BinaryTree:
    def __init__(self, value, parent=None):

        self.left = None
        self.right = None
        self.value = value
        self.parent = parent

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinaryTree(value, self.value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinaryTree(value, self.value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def insert_tree(self, tree):
        value = tree.value
        if value:
            if value < self.value:
                if self.left is None:
                    self.left = BinaryTree(value, self.value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinaryTree(value, self.value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def search(self, value):
        if value < self.value:
            if self.left is None:
                return str(value) + " Not Found"
            return self.left.search(value)
        elif value > self.value:
            if self.right is None:
                return str(value) + " Not Found"
            return self.right.search(value)
        else:
            return self

    def remove(self, value):
        value_tree = self.search(value)
        if not type(value_tree) is str:
            if not value_tree.parent is None:
                parent = self.search(value_tree.parent)
                if not type(parent) is str:
                    if not parent.left is None and parent.left.value == value:
                        parent.left = None
                    if not parent.right is None and parent.right.value == value:
                        parent.right = None

                    if not value_tree.left is None:
                        parent.insert(value_tree.left.value)
                    if not value_tree.right is None:
                        parent.insert(value_tree.right.value)
            else:
                if not value_tree.left is None:
                    self.value = value_tree.left.value
                    self.left = value_tree.left.left
                if not value_tree.right is None:
                    self.insert_tree(value_tree.right)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value),
        if self.right:
            self.right.PrintTree()


tree_sort = BinaryTree(random.randint(1, 1000))
i = 0
while i in range(1000):
    tree_sort.insert(i)
    i += 1

now = datetime.now()
i = 0
while i in range(1000):
    tree_sort.search(random.randint(1, 1000))
    i += 1
print(datetime.now()-now)

now = datetime.now()
i = 0
while i in range(1000):
    tree_sort.remove(random.randint(1, 1000))
    i += 1
print(datetime.now()-now)

print("-------------")
tree = BinaryTree(random.randint(1, 1000))
now = datetime.now()
i = 0
while i in range(1000):
    tree.insert(random.randint(1, 1000))
    i += 1
# print(datetime.now()-now)

now = datetime.now()
i = 0
while i in range(1000):
    tree.search(random.randint(1, 1000))
    i += 1
print(datetime.now()-now)

now = datetime.now()
i = 0
while i in range(1000):
    tree.remove(random.randint(1, 1000))
    i += 1
print(datetime.now()-now)
