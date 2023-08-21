import sys

sys.setrecursionlimit(10**9)


def main():
    H = int(input())
    print((H * (12800000 + H)) ** 0.5)


if __name__ == "__main__":
    main()
