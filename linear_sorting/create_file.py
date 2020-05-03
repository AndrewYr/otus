import random
FILENAME = 'file.bin'


def create_file():
    file = open(FILENAME, 'w')
    cur = 0
    while cur <= 1000000000:
        file.write(str(cur)+'\n')
        cur += 1
    file.close()


def get_shuffle_list():
    file = open(FILENAME, 'r')
    lst = [int(line.strip()) for line in file]
    random.shuffle(lst)
    return lst
