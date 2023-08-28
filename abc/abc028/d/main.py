import sys

sys.setrecursionlimit(10**9)


def main():
    N, K = map(int, input().split())

    tot = N**3
    case_ = (K - 1) * (N - K) * 6 + (N - K) * 3 + (K - 1) * 3 + 1
    print(case_ / tot)


if __name__ == "__main__":
    main()
