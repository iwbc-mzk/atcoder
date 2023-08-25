import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = input()

    R = [-1] * (N + 1)
    L = [-1] * (N + 1)

    for i, s in enumerate(S, 1):
        if s == "L":
            R[i], L[i] = i - 1, L[i - 1]
            L[i - 1] = i
            if L[i] != -1:
                R[L[i]] = i

        else:
            R[i], L[i] = R[i - 1], i - 1
            R[i - 1] = i
            if R[i] != -1:
                L[R[i]] = i

    start = -1
    for i, v in enumerate(L):
        if v == -1:
            start = i

    ans = []
    a = start
    while a != -1:
        ans.append(a)
        a = R[a]
    print(*ans)


if __name__ == "__main__":
    main()
