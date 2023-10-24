import sys

sys.setrecursionlimit(10**9)


def main():
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))

    ans = 0
    for i in range(N - 1):
        w = (X[i + 1] - X[i]) * A
        t = B
        ans += min(w, t)

    print(ans)


if __name__ == "__main__":
    main()
