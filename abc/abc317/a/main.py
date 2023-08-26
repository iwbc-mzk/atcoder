import sys

sys.setrecursionlimit(10**9)


def main():
    N, H, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i, p in enumerate(P, 1):
        if p + H >= X:
            print(i)
            return


if __name__ == "__main__":
    main()
