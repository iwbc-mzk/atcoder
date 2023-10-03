import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = input()
    T = input()

    sc, tc = defaultdict(int), defaultdict(int)
    for s, t in zip(S, T):
        sc[s] += 1
        tc[t] += 1

    if sc != tc:
        print(-1)
        return

    l, r = -1, N
    while r - l > 1:
        m = (r + l) // 2

        i = 0
        ok = True
        for v in S[m:]:
            v_ok = False
            for j in range(i, N):
                if T[j] == v:
                    i = j + 1
                    v_ok = True
                    break
            ok &= v_ok

        if ok:
            r = m
        else:
            l = m

    print(r)


if __name__ == "__main__":
    main()
