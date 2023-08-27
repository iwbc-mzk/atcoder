import sys
from itertools import product

sys.setrecursionlimit(10**9)


def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    p = product(*[range(K) for _ in range(N)])

    for v in p:
        t = None
        for i, vv in enumerate(v):
            if not t:
                t = T[i][vv]
            else:
                t ^= T[i][vv]

        if t == 0:
            print("Found")
            return
    else:
        print("Nothing")


if __name__ == "__main__":
    main()
