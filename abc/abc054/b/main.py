import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            for i in range(M):
                for j in range(M):
                    if A[i + r][j + c] != B[i][j]:
                        break
                else:
                    continue
                break
            else:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
