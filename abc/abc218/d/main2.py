def main():
    N = int(input())
    XY = list(tuple(map(int, input().split())) for _ in range(N))
    XY_set = set(XY)

    ans = 0
    for dl in XY:
        for ur in XY:
            if dl[0] >= ur[0] or dl[1] >= ur[1]:
                continue

            dr = (ur[0], dl[1])
            ul = (dl[0], ur[1])
            if dr in XY_set and ul in XY_set:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
