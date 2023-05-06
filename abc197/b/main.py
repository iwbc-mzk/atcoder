def main():
    H, W, X, Y = map(int, input().split())
    X, Y = X-1, Y-1
    S = [list(input()) for _ in range(H)]

    # (X, Y)を含むため初期値は1
    result = 1

    # タテ方向
    up_flg, down_flg, left_flg, right_flg = [True] * 4
    step = 1
    while up_flg or down_flg or left_flg or right_flg:
        # 上
        if up_flg and X-step >= 0 and S[X-step][Y] == ".":
            result += 1
        else:
            up_flg = False
        
        # 下
        if down_flg and X+step < H and S[X+step][Y] == ".":
            result += 1
        else:
            down_flg = False

        # 左
        if left_flg and Y-step >= 0 and S[X][Y-step] == ".":
            result += 1
        else:
            left_flg = False

        # 右
        if right_flg and Y+step < W and S[X][Y+step] == ".":
            result += 1
        else:
            right_flg = False

        step += 1

    print(result)


if __name__ == "__main__":
    main()