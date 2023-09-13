import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7

    C = defaultdict(int)
    for a in A:
        C[a] += 1

    ans = 1
    for k, v in C.items():
        if (k == 0 and v != 1) or (k != 0 and v != 2):
            print(0)
            return
        if (N % 2 != 0 and k % 2 != 0) or (N % 2 == 0 and k % 2 == 0):
            print(0)
            return

        ans *= v
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
