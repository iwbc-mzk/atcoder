import sys
from math import log10, floor

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    MOD = 998244353

    ans = 0
    n = floor(log10(N))
    for i in range(n):
        ans += 9 * 10**i * (1 + 9 * 10**i) // 2
        ans %= MOD

    l = N - 10**n + 1
    ans += l * (1 + l) // 2
    ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
