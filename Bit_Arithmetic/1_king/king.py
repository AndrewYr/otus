l_border = 0xFeFeFeFeFeFeFeFe
nAB = 0xFcFcFcFcFcFcFcFc
r_border = 0x7f7f7f7f7f7f7f7f
nGH = 0x3f3f3f3f3f3f3f3f


def get_result(x: int):
    start = 1 << x
    p9 = (start & r_border) << 9
    p8 = start << 8
    p7 = (start & l_border) << 7
    p6 = (start & r_border) << 1
    p4 = (start & l_border) >> 1
    p3 = (start & r_border) >> 7
    p2 = start >> 8
    p1 = (start & l_border) >> 9
    movesBits = p9 | p8 | p7 | p6 | p4 | p3 | p2 | p1
    b = movesBits
    q = 0
    while movesBits > 0:
        if 1 == (movesBits & 1):
            q += 1
        movesBits >>= 1
    return q, b

