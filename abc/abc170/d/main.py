import sys
from collections import defaultdict

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
    A = list(map(int, input().split()))

    AA = defaultdict(int)
    for a in A:
        AA[a] += 1

    ans = 0
    for a in A:
        ed = enumerate_divisors(a)
        for i in ed:
            if i in AA:
                if i == a and AA[i] == 1:
                    continue
                break

        else:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
