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


def main():
    N = int(input())

    pr = prime_factorization(N)

    ans = math.ceil(math.log2(sum(pr.values())))
    print(ans)


if __name__ == "__main__":
    main()
