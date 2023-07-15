def main():
    N = int(input())
    S = input()


    SS = []
    for i, s in enumerate(S):
        if i == 0:
            SS.append(int(s))
        else:
            if SS[i - 1] == 1 and int(s) == 1:
                SS.append(0)
            else:
                SS.append(1)

    SSS = [0]
    for i, s in enumerate(SS, 1):
        SSS.append(SSS[i - 1] + s)


    ans = 0
    for i in range(1, N + 1):
        ans += SSS[N] - SSS[i - 1]

    pass


if __name__ == "__main__":
    main()
