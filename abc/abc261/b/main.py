def main():
    N = int(input())
    A = [list(input()) for _ in range(N)]

    ans = True
    for i in range(N):
        for j in range(i + 1, N):
            if A[i][j] == "W" and A[j][i] != "L":
                ans = False
            if A[i][j] == "L" and A[j][i] != "W":
                ans = False
            if A[i][j] == "D" and A[j][i] != "D":
                ans = False

            if not ans:
                break

        if not ans:
            break

    print("correct" if ans else "incorrect")


if __name__ == "__main__":
    main()
