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
    K = int(input())

    ed = enumerate_divisors(K)

    ans = 0
    for ai in range(len(ed)):
        a = ed[ai]

        for bi in range(ai, len(ed)):
            b = ed[bi]

            if a * b > K or K % (a * b) or b > K // (a * b):
                continue

            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
