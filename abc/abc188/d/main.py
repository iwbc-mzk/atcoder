def main():
    N, C = map(int, input().split())

    event = []
    for _ in range(N):
        ai, bi, ci = map(int, input().split())
        event.append((ai, ci))
        event.append((bi + 1, -ci))

    event.sort(key=lambda x: x[0])
    t = 0
    curr = 0
    ans = 0
    for ti, vi in event:
        ans += min(curr, C) * (ti - t)
        t = ti
        curr += vi

    print(ans)


if __name__ == "__main__":
    main()
