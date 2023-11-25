import sys

sys.setrecursionlimit(10**9)


def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    ans = []
    for a in A:
        if L <= a <= R:
            ans.append(a)
        else:
            if abs(R - a) < abs(L - a):
                ans.append(R)
            else:
                ans.append(L)

    print(*ans)


if __name__ == "__main__":
    main()
