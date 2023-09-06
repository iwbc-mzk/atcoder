import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())

    ans = (-1, -1)
    for i in range(1, 10):
        t = 0
        for j in range(N):
            t = (t * 10 + i) % M

            if t == 0:
                ans= max(ans, (j + 1, i))

    if ans != (-1, -1):
        print(str(ans[1]) * ans[0])
    else:
        print(-1)


if __name__ == "__main__":
    main()
