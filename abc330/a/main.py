import sys

sys.setrecursionlimit(10**9)


def main():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    for a in A:
        if a >= L:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
