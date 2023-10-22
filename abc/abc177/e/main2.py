import sys
from collections import defaultdict
import math


# 計算量O(√N)
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


sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    if math.gcd(*A) != 1:
        print("not coprime")
        return

    C = defaultdict(int)
    for a in A:
        pf = prime_factorization(a)
        for key in pf.keys():
            C[key] += 1
            if C[key] > 1:
                print("setwise coprime")
                return
    else:
        print("pairwise coprime")


if __name__ == "__main__":
    main()
