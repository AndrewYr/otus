from time import time
class VArray:
    lst = []
    size = 0
    vector = 0

    def __init__(self, vector=100):
        self.vector = vector

    def resize(self, size):
        self.lst = self.lst + ([None] * size)
        return self

    def get_size(self):
        return len(self.lst)

    def add(self, item):
        if self.get_size() == self.size:
            self.resize(self.vector)
        self.lst[self.size] = item
        self.size += 1
        return self


new_array = VArray(100)
start_time = time()
for i in range(10000):
    new_array.add(i)
print(time()-start_time)

start_time = time()
for i in range(10000):
    for index in sorted(new_array.lst, reverse=True):
        del(new_array.lst[index])
print(time() - start_time)
