def main():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]

    event = []
    for a, b in AB:
        event.append((a, 1))
        event.append((a + b, -1))
    event.sort(key=lambda x: x[0])

    ans = [0 for _ in range(N)]
    curr = 0
    t_curr = 0
    for t, v in event:
        if t != t_curr and curr:
            ans[curr - 1] += t - t_curr
        curr += v
        t_curr = t

    print(*ans)


if __name__ == "__main__":
    main()
