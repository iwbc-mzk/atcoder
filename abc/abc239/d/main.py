import sys

sys.setrecursionlimit(10**9)

import math


# 計算量O(√N)
def prime_factorization(n: int):
    result = []
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        # 割り切れるだけ割る
        while n % i == 0:
            n //= i
            result.append(i)

        if n == 1:
            break

    # 最後に残った商が1より大きければ、これが√Nより大きい唯一の素因数になる
    if n > 1:
        result.append(n)

    return result


def main():
    A, B, C, D = map(int, input().split())

    for i in range(A, B + 1):
        aoki_win = False
        for j in range(C, D + 1):
            v = i + j
            p = prime_factorization(v)
            if len(p) == 1:
                aoki_win = True

            if aoki_win:
                break
        else:
            print("Takahashi")
            return
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
