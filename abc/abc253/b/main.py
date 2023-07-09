def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    c = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                c.append((i, j))

    print(abs(c[0][0] - c[1][0]) + abs(c[0][1] - c[1][1]))


if __name__ == "__main__":
    main()
