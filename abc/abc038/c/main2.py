import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    l, r = 0, 0
    ans = 0
    while l < N:
        while r + 1 < N and A[r + 1] > A[r]:
            r += 1
        ans += r - l + 1
        l += 1
        if l == r + 1:
            r += 1

    print(ans)


if __name__ == "__main__":
    main()
