import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())

    D = defaultdict(list)
    y = []
    for _ in range(M):
        P, Y = map(int, input().split())
        D[P].append(Y)
        y.append(Y)

    ans = defaultdict()
    for key, val in D.items():
        val.sort()
        for i, v in enumerate(val, 1):
            id = str(key).zfill(6) + str(i).zfill(6)
            ans[v] = id

    for i in y:
        print(ans[i])


if __name__ == "__main__":
    main()
