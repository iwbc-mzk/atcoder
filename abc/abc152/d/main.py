import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    D = defaultdict(lambda: defaultdict(set))
    for i in range(1, N + 1):
        ii = str(i)
        D[ii[0]][ii[-1]].add(i)

    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            ii, jj = str(i), str(j)
            ans += len(D[ii][jj]) * len(D[jj][ii])

    print(ans)


if __name__ == "__main__":
    main()
