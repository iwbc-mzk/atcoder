from math import gcd


def main():
    A, B, C = map(int, input().split())

    m = gcd(A, B)
    m = gcd(m, C)

    ans = 0
    for i in [A, B, C]:
        ans += i // m - 1

    print(ans)


if __name__ == "__main__":
    main()
