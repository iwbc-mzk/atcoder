def main():
    N = int(input())
    ST = [tuple(input().split()) for _ in range(N)]

    for i in range(N):
        si, ti = ST[i]
        si_flg = False
        ti_flg = False
        for j in range(N):
            stj = ST[j]
            if i == j:
                continue

            if si in stj:
                si_flg = True
            if ti in stj:
                ti_flg = True

            if si_flg and ti_flg:
                print("No")
                return
    else:
        print("Yes")


if __name__ == "__main__":
    main()
