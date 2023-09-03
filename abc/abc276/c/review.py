def main():
    N = int(input())
    P = list(map(int, input().split()))

    ans = ""
    for i in range(N - 1, 0, -1):
        p1, p2 = P[i], P[i - 1]
        if p1 < p2:
            t = 0
            for p in P[i - 1 :]:
                if p < p2:
                    t = max(t, p)

            s = [x for x in P[i - 1 :] if x != t]
            s.sort(reverse=True)

            ans = P[: i - 1] + [t] + s
            break

    print(*ans)


if __name__ == "__main__":
    main()
