def main():
    N, Q = map(int, input().split())

    idx = {v: i for i, v in enumerate(range(1, N + 1))}
    ball = [i for i in range(1, N + 1)]
    for _ in range(Q):
        x = int(input())
        i = idx[x]
        if i == N - 1:
            xx = ball[i - 1]
            ball[i - 1], ball[i] = x, xx
            idx[x], idx[xx] = i - 1, i
        else:
            xx = ball[i + 1]
            ball[i], ball[i + 1] = xx, x
            idx[x], idx[xx] = i + 1, i

    print(*ball)


if __name__ == "__main__":
    main()
