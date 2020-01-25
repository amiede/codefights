# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/W5Sq7taLSzNHh8GiF
# Solution by nickie
from itertools import permutations

def crosswordFormation(W):
    def count(a, b, c, d):
        # words a and b are horizontal (top to bottom)
        # words c and d are vertical (left to right)
        La, Lb, Lc, Ld = map(len, [a, b, c, d])
        # x is the distance between a and b
        # y is the distance between c and d
        result = 0
        for x in range(2, min(La, Lb)):
            top = [(a[i], a[i+x]) for i in range(La-x)]
            bottom = [(b[i], b[i+x]) for i in range(Lb-x)]
            for y in range(2, min(Lc, Ld)):
                left = [(c[i], c[i+y]) for i in range(Lc-y)]
                right = [(d[i], d[i+y]) for i in range(Ld-y)]
                for ul, ur in top:
                    for bl, br in bottom:
                        n1 = left.count((ul, bl))
                        n2 = right.count((ur, br))
                        result += n1 * n2
        return result
    return 2 * sum(count(W[0], w1, w2, w3) + count(w1, W[0], w2, w3)
                   for w1, w2, w3 in permutations(W[1:]))

