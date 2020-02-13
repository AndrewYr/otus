nA = 0xFeFeFeFeFeFeFeFe
nAB = 0xFcFcFcFcFcFcFcFc
nH = 0x7f7f7f7f7f7f7f7f
nGH = 0x3f3f3f3f3f3f3f3f


def get_result(x: int):
    start = 1 << x
    p8 = nGH & (start << 6 | start >> 10)
    p6 = nH & (start << 15 | start >> 17)
    p4 = nA & (start << 17 | start >> 15)
    p2 = nAB & (start << 10 | start >> 6)
    movesBits = p8 | p6 | p4 | p2
    b = movesBits
    q = 0
    while movesBits > 0:
        if 1 == (movesBits & 1):
            q += 1
        movesBits >>= 1
    return q, b
