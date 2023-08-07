def main():
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))
    C = tuple(map(int, input().split()))
    D = tuple(map(int, input().split()))

    def vec(a, b):
        return (b[0] - a[0], b[1] - a[1])

    # ベクトルの外積が >0 のとき180度未満、 <=0 の時180度以上
    def judge(vec1, vec2):
        cp = vec1[0] * vec2[1] - vec1[1] * vec2[0]
        if cp > 0:
            return True
        else:
            return False

    AB = vec(A, B)
    AD = vec(A, D)
    if not judge(AB, AD):
        print("No")
        return

    BC = vec(B, C)
    BA = vec(B, A)
    if not judge(BC, BA):
        print("No")
        return

    CD = vec(C, D)
    CB = vec(C, B)
    if not judge(CD, CB):
        print("No")
        return

    DA = vec(D, A)
    DC = vec(D, C)
    if not judge(DA, DC):
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
