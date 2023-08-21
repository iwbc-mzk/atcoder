import sys
from collections import defaultdict


sys.setrecursionlimit(10**9)


def main():
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))

    G = defaultdict(set)
    for _ in range(N):
        A, B = map(int, input().split())
        if A > B:
            A, B = B, A
        G[A].add(B)

    dp = [[-1] * 21 for _ in range(N + 1)]
    



if __name__ == "__main__":
    main()
