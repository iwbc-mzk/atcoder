from math import gcd


def main():
    L, R = map(int, input().split())

    # y - x のR - Lからの変化
    for i in range(R - L):
        # iの内xの変化分
        for j in range(i + 1):
            x = L + j
            y = R - (i - j)

            if gcd(x, y) == 1:
                print(y - x)
                return


if __name__ == "__main__":
    main()
