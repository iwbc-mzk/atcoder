import sys

sys.setrecursionlimit(10**9)


def main():
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))

    CS = [set([c]) for c in C]

    for _ in range(Q):
        a, b = map(int, input().split())
        if len(CS[b - 1]) > len(CS[a - 1]):
            CS[b - 1].update(CS[a - 1])
            CS[a - 1] = set()
        else:
            CS[a - 1].update(CS[b - 1])
            CS[b - 1], CS[a - 1] = CS[a - 1], set()

        print(len(CS[b - 1]))


if __name__ == "__main__":
    main()
