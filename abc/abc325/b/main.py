import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    WX = [tuple(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(24):
        if i == 20:
            pass
        c = 0
        for w, x in WX:
            t = (i + x) % 24
            if 9 <= t <= 17:
                c += w
        ans = max(ans, c)

    print(ans)


if __name__ == "__main__":
    main()
