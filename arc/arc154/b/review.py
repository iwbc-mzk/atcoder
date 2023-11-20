def main():
    N = int(input())
    S = input()
    T = input()

    if S == T:
        print(0)
        return

    if sorted(S) != sorted(T):
        print(-1)
        return

    l, r = 0, N
    while r - l > 1:
        m = (l + r) // 2

        si = m
        for i in range(N):
            if S[si] == T[i]:
                si += 1

            if si == N:
                break

        if si == N:
            r = m
        else:
            l = m

    print(r)


if __name__ == "__main__":
    main()
