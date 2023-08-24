import sys

sys.setrecursionlimit(10**9)


def main():
    n = int(input())
    print("Yes" if 2**n > n**2 else "No")


if __name__ == "__main__":
    main()
