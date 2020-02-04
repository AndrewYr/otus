from time import process_time
'''
4. Алгоритм поиска чисел Фибоначчи макс. 6 байта
4a. Через рекурсию
+1 байт 4b. Через итерацию
+1 байт 4c. По формуле золотого сечения
+2 байт 4d. Через умножение матриц
+2 байт Составить сравнительную таблицу времени работы алгоритмов для разных начальных данных.
Написать, какие пункты выполнены и сколько времени ушло на выполнение домашнего задания.
'''

# 4a. Через рекурсию
def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)


# 4a. Через рекурсию
print(fib(5))
# время 1.2517999999999557e-05
print(fib(35))
# время 2.216459865


# 4b. Через итерацию
def fib(n):
    def fibIter(a, b, count):
        if count==0:
            return b
        else:
            return fibIter(a+b, a, count-1)
    return fibIter(1, 0, n)
# 4b. Через итерацию
print(fib(5))
# 7.856000000083796e-06
print(fib(35))
# 9.912999999972527e-06

# 4c. По формуле золотого сечения
PHI = 1.6180339
f = [0, 1, 1, 2, 3, 5]
def fib_gold(n):
    if n < 6:
        return f[n]

    t = 5
    fn = 5

    while t < n:
        fn = round(fn * PHI)
        t += 1

    return fn

# 4c. По формуле золотого сечения
print(fib_gold(5))
# 4.858000000051987e-06

print(fib_gold(35))
# 1.9446000000034047e-05



# 4d. Через умножение матриц
F1 = [1, 1,
      1, 0]
def matrix_multiply(A, B):
    a, b, c, d = A
    x, y, z, w = B

    return (
        a * x + b * z,
        a * y + b * w,
        c * x + d * z,
        c * y + d * w,
    )


def naive_matrix_power(A, m):
    if m == 0:
        return [1, 0, 0, 1]
    B = A
    for _ in range(m - 1):
        B = matrix_multiply(B, A)
    return B

def naive_matrix_fib(n):
    return naive_matrix_power(F1, n)[1]

# 4d. Через умножение матриц
print(naive_matrix_fib(5))
# время 9.02000000002623e-06

print(naive_matrix_fib(35))
# время 1.5050000000016439e-05

'''На выполнение ДЗ ушло 60 мин
Выполнено 4a 4b 4c 4d
Время работы написано после каждой функции
'''