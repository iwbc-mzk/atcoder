from collections import defaultdict

def main():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))

    A_max = max(A)
    r = N * A_max

    dp_x = [[False for _ in range(-r, r + 1)].copy() for _ in range(N + 1)]
    dp_x[0][0] = True
    dp_y = [[False for _ in range(-r, r + 1)].copy() for _ in range(N + 1)]
    dp_y[0][0] = True
    for i in range(1, N + 1):
        if i == 1:
            dp_x[i][A[i - 1]] = True
            continue

        if i % 2:
            a = A[i - 1]
            for x in range(-r, r + 1):
                dp_x[i][x] = dp_x[i - 2][x + a] or dp_x[i - 2][x - a]
        else:
            pass
            a = A[i - 1]
            for y in range(-r, r + 1):
                dp_y[i][y] = dp_y[i - 2][y + a] or dp_y[i - 2][y - a]
    
    if N % 2:
        print("Yes" if dp_x[N][X] and dp_y[N - 1][Y] else "No")
    else:
        print("Yes" if dp_x[N - 1][X] and dp_y[N][Y] else "No")


if __name__ == "__main__":
    main()