import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    B = [list(map(int, list(input()))) for _ in range(N)]

    A = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i in [0, N - 1] or j in [0, M - 1]:
                A[i][j] = 0
                continue

            m = float("inf")
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ii = i + di
                jj = j + dj
                m = min(m, B[ii][jj])

            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ii = i + di
                jj = j + dj
                B[ii][jj] -= m

            A[i][j] = m

    for a in A:
        print("".join(map(str, a)))


if __name__ == "__main__":
    main()
