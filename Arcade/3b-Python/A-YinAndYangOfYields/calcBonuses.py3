# https://app.codesignal.com/arcade/python-arcade/yin-and-yang/z6KZcoJ9jePsenzWo
def calcBonuses(bonuses, n):
    it = (b for b in bonuses)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res
