def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]
    T = [list(input()) for _ in range(N)]

    SS = set((i, j) for i in range(N) for j in range(N) if S[i][j] == "#")
    TT = set((i, j) for i in range(N) for j in range(N) if T[i][j] == "#")

    if len(SS) != len(TT):
        print("No")
        return

    for r in range(4):
        for di in range(-200, 200):
            for dj in range(-200, 200):
                for i, j in SS:
                    for _ in range(r):
                        i, j = j, -i

                    ii, jj = i + di, j + dj
                    if (ii, jj) not in TT:
                        break
                else:
                    print("Yes")
                    return

    print("No")


if __name__ == "__main__":
    main()
