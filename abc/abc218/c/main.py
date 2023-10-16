def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]

    s_cnt = sum([s.count("#") for s in S])
    t_cnt = sum([t.count("#") for t in T])
    if s_cnt != t_cnt:
        print("No")
        return

    SXY = [(x, y) for x in range(N) for y in range(N) if S[x][y] == "#"]

    for i in range(4):
        for dx in range(-N + 1, N):
            for dy in range(-N + 1, N):
                for x, y in SXY:
                    xx, yy = x, y
                    for _ in range(i):
                        xx, yy = yy, N - xx - 1

                    xx, yy = xx + dx, yy + dy
                    if not (0 <= xx < N) or not (0 <= yy < N):
                        if S[x][y] == "#":
                            break
                        else:
                            continue

                    if S[x][y] != T[xx][yy]:
                        break
                else:
                    print("Yes")
                    return

    print("No")


if __name__ == "__main__":
    main()
