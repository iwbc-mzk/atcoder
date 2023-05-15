def main():
    N = int(input())
    S = [input() for _ in range(N)]

    for x in range(N):
        for y in range(N):
            for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                cnt = 0
                for i in range(6):
                    if not (0 <= x + i * dx < N):
                        break

                    if not (0 <= y + i * dy < N):
                        break

                    if S[x + i * dx][y + i * dy] == "#":
                        cnt += 1
                else:       
                    if cnt >= 4:
                        print("Yes")
                        return

    else:
        print("No")


if __name__ == "__main__":
    main()
