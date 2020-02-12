from horse import get_result

path = 'Bitboard/'


def go():
    num_file = 0
    while True:
        try:
            with open(f'{path}test.{num_file}.in', 'r') as read_file:
                in_file = int(read_file.readline())
                read_file.close()
            with open(f'{path}test.{num_file}.out', 'r') as read_file:
                out_file = read_file.read().split('\n')

            run_test(in_file, out_file, num_file)
            num_file += 1

        except IOError as e:
            print(f'файл с номером {num_file} не найден')
            break


def run_test(in_file, out_file, num_test):
    k, g = get_result(in_file)
    if int(out_file[0]) == k and int(out_file[1]) == g:
        print(f'Test#{num_test} True')
    else:
        print(f'Test#{num_test} False')


if __name__ == '__main__':
    go()
