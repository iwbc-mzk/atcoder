def main():
    N = int(input())

    lr = []
    max_r = 0
    for _ in range(N):
        L, R = map(int, input().split())
        lr.append((L, 1))
        lr.append((R, -1))
        max_r = max(max_r, R)

    t = [0 for _ in range(max_r + 1)]
    for s, v in lr:
        t[s] += v

    ans = []
    l = None
    for i in range(1, max_r + 1):
        t[i] += t[i - 1]
        if t[i] == 0 and l:
            ans.append((l, i))
            l = None

        if t[i] > 0 and not l:
            l = i

    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()
