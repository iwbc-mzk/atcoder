import sys
from collections import defaultdict
import math

sys.setrecursionlimit(10**9)


def prime_factorization(n: int):
    result = defaultdict(int)
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        # 割り切れるだけ割る
        while n % i == 0:
            n //= i
            result[i] += 1

        if n == 1:
            break

    # 最後に残った商が1より大きければ、これが√Nより大きい唯一の素因数になる
    if n > 1:
        result[n] = 1

    return result


def main():
    N = int(input())
    MOD = 10**9 + 7
    C = defaultdict(int)
    ans = 1
    for n in range(N, 0, -1):
        pf = prime_factorization(n)
        for key, v in pf.items():
            C[key] += v

    for key, v in C.items():
        ans *= v + 1
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
