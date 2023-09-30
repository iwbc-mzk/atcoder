import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = input()

    print(S.find("ABC") + 1 if "ABC" in S else -1)


if __name__ == "__main__":
    main()
