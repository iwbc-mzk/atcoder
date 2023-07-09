from typing import List


# 参考: https://ikatakos.com/pot/programming_algorithm/number_theory/prime_judge
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
        primes = list(primes)

        return primes


def main():
    N = int(input())

    p_nums = sieve_of_eratosthenes(10**6)
    p_nums.sort()

    ans = 0
    for i in range(len(p_nums)):
        p = p_nums[i]

        left = i + 1
        right = len(p_nums) - 1

        if p * p_nums[left] ** 3 > N:
            break

        while right - left > 1:
            mid = (right + left) // 2
            q = p_nums[mid]
            if p * q**3 <= N:
                left = mid
            else:
                right = mid

        ans += left - i

    print(ans)


if __name__ == "__main__":
    main()
