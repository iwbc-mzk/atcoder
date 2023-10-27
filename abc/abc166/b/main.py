import sys

sys.setrecursionlimit(10**9)


def main():
    N, K = map(int, input().split())
    A = [0 for _ in range(N)]
    for _ in range(K):
        _ = input()
        a = map(int, input().split())
        for ai in a:
            A[ai - 1] += 1

    print(A.count(0))


if __name__ == "__main__":
    main()
