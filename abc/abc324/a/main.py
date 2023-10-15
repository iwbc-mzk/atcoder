import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = set(map(int, input().split()))

    print("Yes" if len(A) == 1 else "No")


if __name__ == "__main__":
    main()
