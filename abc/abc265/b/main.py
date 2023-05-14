def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = {}
    X = set()
    for _ in range(M):
        x, y = map(int, input().split())
        XY[x - 1] = y
        X.add(x - 1)

    for i in range(N - 1):
        if i in X:
            T += XY[i]
        
        T -= A[i]
        if T <= 0:
            break

    if T > 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()