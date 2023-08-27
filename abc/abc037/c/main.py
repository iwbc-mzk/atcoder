import sys

sys.setrecursionlimit(10**9)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    t = 0
    for i in range(N):
        if i < K:
            t += A[i]
        else:
            t += A[i]
            t -= A[i - K]

        if i >= K - 1:
            ans += t

    print(ans)


if __name__ == "__main__":
    main()
