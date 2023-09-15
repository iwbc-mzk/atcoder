import sys

sys.setrecursionlimit(10**9)


def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))

    ans = float("inf")
    for l in range(N - K + 1):
        r = l + K - 1

        x1 = abs(X[l]) + abs(X[l] - X[r])
        x2 = abs(X[r]) + abs(X[r] - X[l])
        ans = min(ans, min(x1, x2))

    print(ans)


if __name__ == "__main__":
    main()
