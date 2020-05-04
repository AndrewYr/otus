import random
from create_file import get_shuffle_list
from datetime import datetime


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


lst = [i for i in range(32)]
random.shuffle(lst)
now = datetime.now()
quicksort(lst)
print(datetime.now()-now)
# 0:00:00.000080

lst = [i for i in range(600)]
random.shuffle(lst)
now = datetime.now()
quicksort(lst)
print(datetime.now()-now)
# 0:00:00.001728

lst = [i for i in range(1024)]
random.shuffle(lst)
now = datetime.now()
quicksort(lst)
print(datetime.now()-now)
# 0:00:00.002794

start_time = datetime.now()
quicksort(get_shuffle_list())
print(datetime.now()-start_time)
# 0:00:56.853887
