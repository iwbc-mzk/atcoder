import sys

sys.setrecursionlimit(10**9)


def main():
    N, S, M, L = map(int, input().split())

    ans = float("inf")
    for s in range(N // 6 + 10):
        for m in range(N // 8 + 10):
            for l in range(N // 12 + 10):
                p = S * s + M * m + L * l
                n = 6 * s + 8 * m + 12 * l
                if n >= N:
                    ans = min(ans, p)

    print(ans)


if __name__ == "__main__":
    main()
