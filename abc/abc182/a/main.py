import sys

sys.setrecursionlimit(10**9)


def main():
    A, B = map(int, input().split())
    print(2 * A + 100 - B)


if __name__ == "__main__":
    main()
