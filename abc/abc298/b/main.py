def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(N)]

    for k in range(4):
        flg = True
        for i in range(N):
            for j in range(N):
                if not A[i][j]:
                    continue
                
                if k == 0:
                    ii = i
                    jj = j
                if k == 1:
                    ii = N - 1 - j
                    jj = i
                if k == 2:
                    ii = N - 1 - i
                    jj = N - 1 - j
                if k == 3:
                    ii = j
                    jj = N - 1 - i
                if A[i][j] != B[ii][jj]:
                    flg = False
                    break
        if flg:
            print("Yes")
            break
    else:
        print("No")
                    



if __name__ == "__main__":
    main()