import sys

sys.setrecursionlimit(10**9)


def main():
    A, B, C, D = map(int, input().split())

    if A > C:
        print("Aoki")
    elif A < C:
        print("Takahashi")
    else:
        if B > D:
            print("Aoki")
        else:
            print("Takahashi")


if __name__ == "__main__":
    main()
