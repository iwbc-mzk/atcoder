import sys

sys.setrecursionlimit(10**9)


def main():
    N, T = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    ans = 0
    o, c = -1, -1
    for a in A:
        if o == -1 and c == -1:
            o = a
            c = a + T
        else:
            if c < a:
                ans += T
            else:
                ans += a - o

            o = a
            c = a + T
    else:
        ans += c - o

    print(ans)


if __name__ == "__main__":
    main()
