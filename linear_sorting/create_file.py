import random
FILENAME = 'file.txt'


def create_file():
    file = open(FILENAME, 'w')
    cur = 0
    while cur <= 10000000:
        file.write(str(cur)+'\n')
        cur += 1
    file.close()


def get_shuffle_list():
    file = open(FILENAME, 'r')
    lst = [int(line.strip()) for line in file]
    random.shuffle(lst)
    return lst

create_file()