import sys
from math import log10, floor

sys.setrecursionlimit(10**9)


def calc(s, n, d, plus: bool):
    t = 0
    while n >= 0:
        if (plus and s > 9) or (not plus and s < 0):
            break

        t += s * 10**n
        n -= 1
        if plus:
            s += d
        else:
            s -= d
    else:
        return t

    return float("inf")


def main():
    X = int(input())

    n = len(str(X))
    s = int(str(X)[0])

    ans = float("inf")
    while ans == float("inf"):
        d = 0
        while d <= 9:
            c = calc(s, n - 1, d, True)
            if c >= X:
                ans = min(ans, c)
            c = calc(s, n - 1, d, False)
            if c >= X:
                ans = min(ans, c)
            d += 1
        s += 1

    print(ans)


if __name__ == "__main__":
    main()
