def main():
    S = input()
    T = input()

    si, ti = 0, 0
    while ti < len(T):
        if si < len(S) and S[si] == T[ti]:
            si += 1
            ti += 1
        else:
            if T[ti] == S[si - 1] == S[si - 2]:
                ti += 1
            else:
                print("No")
                return
    else:
        if si == len(S) and ti == len(T):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
