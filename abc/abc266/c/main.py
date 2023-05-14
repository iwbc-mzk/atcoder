def main():
    T = [tuple(map(int, input().split())) for _ in range(4)]

    A = T[0]
    B = T[1]
    C = T[2]
    D = T[3]
    
    ans = True

    # A-C対角線
    if A[0] - C[0] == 0:
        t = 0
    else:    
        t = (A[1] - C[1]) / (A[0] - C[0])
    f = lambda x: t * x + A[1] - t * A[0]
    ans &= (B[1] - f(B[0])) * (D[1] - f(D[0])) < 0

    # B-D対角線
    if B[0] - D[0] == 0:
        t = 0
    else:
        t = (B[1] - D[1]) / (B[0] - D[0])
    f = lambda x: t * x + B[1] - t * B[0]
    ans &= (A[1] - f(A[0])) * (C[1] - f(C[0])) < 0

    print("Yes" if ans else "No")


if __name__ == "__main__":
    main()