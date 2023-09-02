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
    K = int(input())

    pf = prime_factorization(K)

    ans = 0
    # 求めるN!はKの倍数 => 各素数のv乗の倍数
    # 各素数に対してnを求めて、最大のものをNとすればそれが答えになる。
    # (n1 < n2 の時 n1! は n2!に必ず含まれる)
    for p, v in pf.items():
        c = 0 # 素数pの出現数

        # 素数の出現数が変化するのは素数の倍数の時のみ
        for a in range(1, v + 1):
            n = p * a
            pp = n
            while pp % p == 0:
                pp //= p
                c += 1

            if c >= v:
                ans = max(ans, n)
                break

    print(ans)


if __name__ == "__main__":
    main()
