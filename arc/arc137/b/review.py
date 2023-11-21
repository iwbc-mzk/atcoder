def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 累積和: S[r]=0~rまでをflipした時に得るスコア
    S = [0]
    for a in A:
        S.append(S[-1] + (-1 if a else 1))

    # S[0]~S[r]までのS[i]の最小値/最大値
    mins, maxs = 0, 0
    # スコア変動の最小値/最大値 => この間の値は全て取りうる値
    low, up = 0, 0

    # rightを固定して最小/最大となるleftを求める
    for s in S:
        low = min(low, s - maxs)
        up = max(up, s - mins)

        mins = min(mins, s)
        maxs = max(maxs, s)

    print(up - low + 1)


if __name__ == "__main__":
    main()
