def main():
    N, D = map(int, input().split())
    S = [input() for _ in range(N)]

    ans = 0
    t = 0
    for d in range(D):
        for s in S:
            if s[d] != "o":
                ans = max(ans, t)
                t = 0
                break
        else:
            t += 1
    else:
        ans = max(ans, t)

    print(ans)


if __name__ == "__main__":
    main()
