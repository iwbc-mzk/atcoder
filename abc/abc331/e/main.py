import sys

sys.setrecursionlimit(10**9)


def main():
    N, M, L = map(int, input().split())
    A = list(map(int, input().split()))
    AA = [(a, i) for i, a in enumerate(A, 1)]
    AA.sort(reverse=True)
    A.sort()
    B = list(map(int, input().split()))
    BB = [(b, i) for i, b in enumerate(B, 1)]
    BB.sort(reverse=True)
    CD = set()
    for _ in range(L):
        C, D = map(int, input().split())
        CD.add((C, D))

    max
    l, r = 0, max(A) + max(B) + 1
    while r - l > 1:
        m = (l + r) // 2

        flg = False
        for a, i in AA:
            for b, j in BB:
                if a + b < m:
                    break

                if (i, j) not in CD and a + b >= m:
                    l = m
                    flg = True
                    break

            if flg:
                break
        else:
            r = m

    print(l)


if __name__ == "__main__":
    main()
