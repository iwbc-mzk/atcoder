import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    A = list(map(int, input().split()))

    # Functional Graphは任意の頂点からN回移動すれば必ず閉路上の頂点になる
    s = 1
    for _ in range(N):
        s = A[s - 1]

    root = []
    while A[s - 1] != -1:
        root.append(s)
        (
            A[s - 1],
            s,
        ) = (
            -1,
            A[s - 1],
        )

    print(len(root))
    print(*root)


if __name__ == "__main__":
    main()
