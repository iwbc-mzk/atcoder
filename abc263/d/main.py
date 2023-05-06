def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    sum_a = sum(A)

    diff_l = [0] * (N + 1)
    for i, a in enumerate(A, 1):
        diff_l[i] = diff_l[i - 1] + L - a

    diff_r = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        diff_r[i] = diff_r[i + 1] +  R - A[i]

    ans = 10 ** 15
    min_diff_l = 10 ** 15
    for y in range(N + 1):
        min_diff_l = min(min_diff_l, diff_l[y])
        ans = min(ans, sum_a + diff_r[y] + min_diff_l)

    print(ans)


if __name__ == "__main__":
    main()
