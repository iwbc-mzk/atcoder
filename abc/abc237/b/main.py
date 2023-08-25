import sys

sys.setrecursionlimit(10**9)


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    B = []
    for j in range(W):
        b = []
        for i in range(H):
            b.append(A[i][j])

        B.append(b)

    for b in B:
        print(*b)


if __name__ == "__main__":
    main()
