'''
1. Алгоритм Евклида поиска НОД макс. 4 байта
'''
# 1a. Через вычитание
def eu_subtraction(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)

# 1b Через остаток
def eu_balance(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(a)

# 1c Через битовые операции
def bit(a, b):
    nod = 1
    tmp = 0
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a == 1 or b == 1:
        return 1
    while a != 0 and b != 0:
        if ((a & 1) | (b & 1)) == 0:
            nod <<= 1
            a >>= 1
            b >>= 1
            continue

        if ((a & 1) == 0) and (b & 1):
            a >>= 1
            continue

        if (a & 1) and ((b & 1) == 0):
            b >>= 1
            continue

        if a > b:
            tmp = a
            a = b
            b = tmp

        tmp = a
        a = (b - a) >> 1
        b = tmp

    if a == 0:
        return nod * b
    else:
        return nod * a

# 1a. Через вычитание
eu_subtraction(125, 15)
#время 1.8775999999999862e-05
eu_subtraction(1234567890, 12)
#время 5.405920951

# 1b Через остаток
eu_balance(125, 15)
# время 6.897999999644355e-06
eu_balance(1234567890, 12)
#время 5.15300000003549e-06


# 1c Через битовые операции
print(bit(125, 15))
# время 6.228999999999957e-06

print(bit(1234567890, 12))
# время 1.0819999999999927e-05

'''На выполнение ДЗ ушло 30 мин
Выполнено 1a 1b 1c
Время работы написано после каждой функции

'''