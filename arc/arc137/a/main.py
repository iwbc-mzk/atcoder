from math import gcd


def main():
    L, R = map(int, input().split())

    ans = 0
    for l in range(L, R):
        if R - l < ans:
            break

        for r in range(R, l, -1):
            if r - l < ans:
                break

            if gcd(l, r) == 1:
                ans = max(ans, r - l)
                break

    print(ans)


if __name__ == "__main__":
    main()
