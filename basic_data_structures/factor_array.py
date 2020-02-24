from time import time


class FArray:
    lst = []
    size = 0
    vector = 0
    increase = 0

    def __init__(self, vector=100, increase=2):
        self.vector = vector
        self.increase = increase
        self.lst = self.lst + ([0] * vector)

    def resize(self, increase):
        self.lst = self.lst + ([0] * len(self.lst) * increase)
        return self

    def get_size(self):
        return len(self.lst)

    def add(self, item):
        if self.get_size() == self.size:
            self.resize(self.increase)
        self.lst[self.size] = item
        self.size += 1
        return self

    def remove(self, index):
        del (self.lst[index])


new_array = FArray(100, 2)
start_time = time()
for i in range(10000):
    new_array.add(i)
print(time() - start_time)
start_time = time()
for i in range(10000):
    for index in sorted(new_array.lst, reverse=True):
        new_array.remove(index)
print(time() - start_time)