import sys

sys.setrecursionlimit(10**9)


def main():
    a = int(input())
    b = int(input())
    h = int(input())

    print((a + b) * h // 2)


if __name__ == "__main__":
    main()
