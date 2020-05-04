from create_file import get_shuffle_list
from datetime import datetime

def simple_counting_sort(A):
    scope = max(A) + 1
    C = [0] * scope
    for x in A:
        C[x] += 1
    A[:] = []
    for number in range(scope):
        A += [number] * C[number]

now = datetime.now()
simple_counting_sort(get_shuffle_list())
print(datetime.now()-now)
# 0:00:12.894326
