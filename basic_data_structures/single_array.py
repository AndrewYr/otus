from time import time


class IArray:
    lst = []

    def resize(self):
        return self.lst + [None]

    def size(self):
        return len(self.lst)

    def get(self, index):
        return self.lst[index]

    def add(self, item):
        self.lst = self.resize()
        self.lst[self.size() - 1] = item
        return self

    def remove(self, index):
        del(self.lst[index])


new_i_array = IArray()
start_time = time()
for i in range(10001):
    new_i_array.add(i)
print(time() - start_time)

start_time = time()
for i in range(10001):
    for index in sorted(new_i_array.lst, reverse=True):
        new_i_array.remove(index)
print(time() - start_time)

