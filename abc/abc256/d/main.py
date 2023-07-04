def main():
    N = int(input())

    lr = []
    for _ in range(N):
        L, R = map(int, input().split())
        lr.append((L, 0))
        lr.append((R, 1))

    lr.sort(key=lambda x: (x[0], -x[1]))
    ans = []
    l = None
    r = None
    c = 0
    for v, vv in lr:
        if c == 0 and vv == 0:
            if l and r and r < v:
                ans.append((l, r))
                l = None
                r = None

        if vv == 0:
            c += 1
            if not l:
                l = v
        else:
            c -= 1
            r = v
    else:
        ans.append((l, r))

    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()
