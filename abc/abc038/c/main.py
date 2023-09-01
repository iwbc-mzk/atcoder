import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    l, r = 0, 0
    ans = 0
    pre = -1
    while l < N and r < N:
        if pre < A[r]:
            ans += r - l + 1
            pre = A[r]
            r += 1
        else:
            l = r
            pre = -1

    print(ans)


if __name__ == "__main__":
    main()
