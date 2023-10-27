import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))

    G = defaultdict(set)
    for _ in range(M):
        A, B = map(int, input().split())
        G[A].add(B)
        G[B].add(A)

    ans = [True for _ in range(N)]
    for i in range(1, N + 1):
        if not ans[i - 1]:
            continue

        for j in G[i]:
            if H[i - 1] < H[j - 1]:
                ans[i - 1] = False
                break
            elif H[i - 1] > H[j - 1]:
                ans[j - 1] = False
            else:
                ans[i - 1] = False
                ans[j - 1] = False

    print(sum(ans))


if __name__ == "__main__":
    main()
