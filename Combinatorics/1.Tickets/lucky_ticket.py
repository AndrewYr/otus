k = 0


def get_result(in_file):
    n = int(in_file)

    def next_digit(nr, sum1, sum2):
        global k
        if nr == 2 * n:
            if sum1 == sum2:
                k += 1
            return
        i = 0
        while i <= 9:
            if nr < n:
                next_digit(nr + 1, sum1 + i, sum2)
            else:
                next_digit(nr + 1, sum1, sum2 + i)
            i += 1

    next_digit(0, 0, 0)
    return str(k)
