import sys
import math

sys.setrecursionlimit(10**9)


def enumerate_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    N = int(input())

    ed = enumerate_divisors(N)
    ans = float("inf")
    for a in ed:
        b = N // a

        ai = math.floor(math.log10(a)) + 1
        bi = math.floor(math.log10(b)) + 1

        ans = min(ans, max(ai, bi))

    print(ans)


if __name__ == "__main__":
    main()
