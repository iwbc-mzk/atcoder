def main():
    N, M = map(int, input().split())

    ans = []
    def rec(i: int, l: list):
        if len(l) == N:
           ans.append(l)
           return

        if i <= M:
            if len(l) < N:
                rec(i + 1, l.copy() + [i])
            rec(i + 1, l.copy())

    rec(1, [])
    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()