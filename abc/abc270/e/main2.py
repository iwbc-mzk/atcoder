def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    l, r = 0, K
    while r - l > 1:
        m = (l + r) // 2

        total = 0
        for a in A:
            total += min(a, m)

        if total <= K:
            l = m
        else:
            r = m

    k = K
    ans = []
    for a in A:
        k -= min(a, l)
        a = max(0, a - l)
        ans.append(a)
    for i in range(N):
        if k > 0 and ans[i] > 0:
            ans[i] -= 1
            k -= 1

    print(*ans)


if __name__ == "__main__":
    main()
