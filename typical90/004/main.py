def main():
    H, W = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(H)]
    sum_h = list(map(sum, A))
    sum_w = list(map(sum, zip(*A)))

    for i in range(H):
        ans = []
        for j in range(W):
            v = sum_h[i] + sum_w[j] - A[i][j]
            ans.append(v)

        print(*ans)


if __name__ == "__main__":
    main()
