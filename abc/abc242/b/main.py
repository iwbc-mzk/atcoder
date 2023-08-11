import sys

sys.setrecursionlimit(10**9)


def main():
    S = list(input())
    S.sort()
    print("".join(S))


if __name__ == "__main__":
    main()
