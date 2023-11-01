from collections import defaultdict


def main():
    N, K = map(int, input().split())
    MOD = 10**5

    L = defaultdict(list)
    x = N
    for i in range(K):
        if x in L:
            L[x].append(i)
            break

        L[x].append(i)
        y = sum(int(v) for v in str(x))
        x = (x + y) % MOD
    else:
        print(x)
        return

    l = L[x][1] - L[x][0]
    if K < l:
        ans = N
        for _ in range(N):
            y = sum(int(v) for v in str(ans))
            ans = (ans + y) % MOD
    else:
        k = K - L[x][0]
        ans = x
        for _ in range(k % l):
            y = sum(int(v) for v in str(ans))
            ans = (ans + y) % MOD

    print(ans)


if __name__ == "__main__":
    main()
