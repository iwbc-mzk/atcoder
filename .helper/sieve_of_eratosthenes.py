from typing import List


# 参考: 
# https://ikatakos.com/pot/programming_algorithm/number_theory/prime_judge
# https://manabitimes.jp/math/992
# 計算量はO(NloglogN)
def sieve_of_eratosthenes(n: int, return_flg: bool = False) -> List[int]:
    # 偶数は2以外は素数でないので探索候補から外す
    is_prime = [i if i % 2 else 0 for i in range(n + 1)]
    is_prime[0], is_prime[1], is_prime[2] = 0, 0, 2

    for p in range(3, int(n**0.5) + 1, 2):
        if is_prime[p]:
            for q in range(p**2, n + 1, 2 * p):
                is_prime[q] = 0

    if return_flg:
        return is_prime
    else:
        primes = set(is_prime)
        primes.remove(0)

        return list(primes)


if __name__ == "__main__":
    print(sieve_of_eratosthenes(10**6))
