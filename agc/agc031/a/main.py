import sys
from itertools import combinations

sys.setrecursionlimit(10**9)


def zord(s):
    return ord(s) - ord("a")


def main():
    N = int(input())
    S = list(input())
    MOD = 10**9 + 7

    A = [0 for _ in range(26)]
    for s in S:
        A[zord(s)] += 1

    ans = 1
    for a in A:
        if a == 0:
            continue

        ans *= 1 + a
        ans %= MOD

    ans -= 1
    ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
