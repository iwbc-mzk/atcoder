from collections import defaultdict


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

    D = defaultdict(int)
    for a in A:
        D[a] += 1

    A_set = set(A)
    ans = 0
    for a in A:
        div = enumerate_divisors(a)
        for d in div:
            if d in A_set and a // d in A_set:
                ans += D[d] * D[a // d]

    print(ans)


if __name__ == "__main__":
    main()
