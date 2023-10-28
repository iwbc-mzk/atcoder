import sys

sys.setrecursionlimit(10**9)


def main():
    X, Y = map(int, input().split())
    if -3 <= Y - X <= 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
