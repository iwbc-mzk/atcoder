import sys

sys.setrecursionlimit(10**9)


def main():
    A, B = map(int, input().split())

    d = A**2 + B**2

    x2 = A**2 / d
    y2 = B**2 / d

    print(x2**0.5, y2**0.5)


if __name__ == "__main__":
    main()
