import sys

sys.setrecursionlimit(10**9)


def main():
    N, M, P = map(int, input().split())

    ans = 1 + (N - M) // P
    print(ans)


if __name__ == "__main__":
    main()
