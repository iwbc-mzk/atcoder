def main():
    N, M = map(int, input().split())
    C = list(input().split())
    D = list(input().split())
    P = list(map(int, input().split()))
    P0 = P[0]
    P = P[1:]
    DP = {}
    for d, p in zip(D, P):
        DP[d] = p

    ans = 0
    for c in C:
        if c in DP:
            ans += DP[c]
        else:
            ans += P0

    print(ans)


if __name__ == "__main__":
    main()
