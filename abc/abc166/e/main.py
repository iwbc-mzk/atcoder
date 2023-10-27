import sys

sys.setrecursionlimit(10**9)
from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))

    # B = defaultdict(int)
    # ans = 0
    # for i in range(1, N + 1):
    #     ans += B[i - A[i - 1]]
    #     B[i + A[i - 1]] += 1

    B = defaultdict(int)
    ans = 0
    for i in range(1, N + 1):
        B[i + A[i - 1]] += 1

    for i in range(1, N + 1):
        ans += B[i - A[i - 1]]

    print(ans)


if __name__ == "__main__":
    main()
