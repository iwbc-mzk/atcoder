import sys

sys.setrecursionlimit(10**9)


def main():
    A, B, C, D = map(int, input().split())
    print(A * B if A * B >= C * D else C * D)


if __name__ == "__main__":
    main()
