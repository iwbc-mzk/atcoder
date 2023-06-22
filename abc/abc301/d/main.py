def main():
    S = input()
    N = int(input())

    def rec(i, v):
        if i >= len(S):
            return v

        if S[i] == "?":
            vv = v + 2 ** (len(S) - i - 1)
            if vv <= N:
                return rec(i + 1, vv)
            else:
                return rec(i + 1, v)
        else:
            return rec(i + 1, v)

    init = 0
    for i, s in enumerate(reversed(S)):
        if s == "1":
            init += 2**i

    ans = rec(0, init)
    print(ans if ans <= N else -1)


if __name__ == "__main__":
    main()
