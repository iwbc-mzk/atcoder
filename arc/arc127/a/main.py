import math


def main():
    N = int(input())

    c = math.log10(N)
    c = math.floor(c) + 1

    ans = 0
    for i in range(1, c + 1):
        l = 0
        for _ in range(i):
            l = 10 * l + 1

        for j in range(c - i + 1):
            left = l * 10**j
            right = (l + 1) * 10**j
            if left > N:
                break

            ans += min(N + 1, right) - left
    print(ans)


if __name__ == "__main__":
    main()
