def get_chess(start: int):
    start += 1
    movesBits = start << 1 | start >> 1 | start << 8 | start << 9 | start >> 8 | start >> 9
    return movesBits


print(get_chess(0))
