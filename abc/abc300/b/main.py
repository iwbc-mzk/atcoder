def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    B = [list(input()) for _ in range(H)]

    for si in range(H):
        for sj in range(W):
            for i in range(H):
                flg = True
                for j in range(W):
                    if A[(i + si) % H][(j + sj) % W] != B[i][j]:
                        flg = False
                        break
                if not flg:
                    break
            else:
                print("Yes")
                return
    else:
        print("No")

if __name__ == "__main__":
    main()