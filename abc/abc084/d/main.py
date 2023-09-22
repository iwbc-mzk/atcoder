import sys
import bisect

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
    Q = int(input())

    primes = []
    for i in range(1, 10**5 + 1, 2):
        a = enumerate_divisors(i)
        if len(a) == 2:
            ii = (i + 1) // 2
            b = enumerate_divisors(ii)
            if len(b) == 2:
                primes.append(i)

    for _ in range(Q):
        l, r = map(int, input().split())

        ll = bisect.bisect_left(primes, l)
        rr = bisect.bisect_right(primes, r)
        print(rr - ll)


if __name__ == "__main__":
    main()
