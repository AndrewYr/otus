import random
import time


def shell_sort(arr):
    n = len(arr)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap = int(gap / 2)


lst = []
i = 0
while i < 700000:
    lst.append(random.randint(0, 1000))
    i += 1
start = time.time()
shell_sort(lst)
print(time.time()-start)
# 10.6316237449646

lst = []
i = 0
while i < 700000:
    lst.append(random.randint(0, 1000))
    if i >= 665000:
        lst.append(random.randint(0, 1000))
    i += 1
start = time.time()
shell_sort(lst)
print(time.time()-start)
# 10.66361379623413
