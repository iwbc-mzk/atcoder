import sys
from collections import deque
from itertools import permutations

sys.setrecursionlimit(10**9)


def main():
    M = int(input())

    S1 = list(map(int, list(input())))
    S2 = list(map(int, list(input())))
    S3 = list(map(int, list(input())))

    A1 = [[] for _ in range(10)]
    A2 = [[] for _ in range(10)]
    A3 = [[] for _ in range(10)]
    for i, (s1, s2, s3) in enumerate(zip(S1, S2, S3), 1):
        A1[s1].append(i)
        A2[s2].append(i)
        A3[s3].append(i)

    A = [A1, A2, A3]

    ans = float("inf")
    for i, j, k in permutations(range(3), 3):
        for v in range(10):
            if not A[i][v] or not A[j][v] or not A[k][v]:
                continue

            ti = A[i][v][0]

            tj = -1
            jj = 0
            while tj == -1 or tj <= ti:
                tj = A[j][v][jj]
                if tj <= ti:
                    A[j][v].append(tj + M)
                jj += 1

            tk = -1
            kk = 0
            while tk == -1 or tk <= tj:
                tk = A[k][v][kk]
                if tk <= tj:
                    A[k][v].append(tk + M)
                kk += 1

            ans = min(ans, tk)

    print(ans - 1 if ans != float("inf") else -1)


if __name__ == "__main__":
    main()
