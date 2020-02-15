l_boarder = 0xFEFEFEFEFEFEFEFE
r_boarder = 0x7F7F7F7F7F7F7F7F
up_boarder = 0x00FFFFFFFFFFFFFF


def get_result(x: int):
    start = 1 << x
    p7 = (up_boarder & (start & l_boarder)) << 7
    p8 = (up_boarder & start) << 8
    p9 = (up_boarder & (start & r_boarder)) << 9
    p4 = (start & l_boarder) >> 1
    p6 = (start & r_boarder) << 1
    p1 = (start & l_boarder) >> 9
    p2 = start >> 8
    p3 = (start & r_boarder) >> 7
    movesBits = p9 | p8 | p7 | p6 | p4 | p3 | p2 | p1
    b = movesBits
    q = 0
    while movesBits > 0:
        q += 1
        movesBits &= movesBits - 1
    return q, b

