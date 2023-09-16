import sys

sys.setrecursionlimit(10**9)


def main():
    A, B = map(int, input().split())
    print(A**B + B**A)


if __name__ == "__main__":
    main()
