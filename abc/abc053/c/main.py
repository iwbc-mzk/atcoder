import sys

sys.setrecursionlimit(10**9)


def main():
    x = int(input())

    i = 2 * (x // 11)
    if x % 11 == 0:
        print(i)
    elif 0 < x % 11 <= 6:
        print(i + 1)
    else:
        print(i + 2)


if __name__ == "__main__":
    main()
