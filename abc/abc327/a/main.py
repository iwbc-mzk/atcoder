import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = input()

    print("Yes" if ("ab" in S or "ba" in S) else "No")


if __name__ == "__main__":
    main()
