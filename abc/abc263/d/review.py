def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    L_cum_sum = [0]
    R_cum_sum = [0]
    L_cum_sum_min = [0]
    R_cum_sum_min = [0]
    for al, ar in zip(A, reversed(A)):
        L_cum_sum.append(L_cum_sum[-1] + (L - al))
        L_cum_sum_min.append(min(L_cum_sum_min[-1], L_cum_sum[-1]))

        R_cum_sum.append(R_cum_sum[-1] + (R - ar))
        R_cum_sum_min.append(min(R_cum_sum_min[-1], R_cum_sum[-1]))

    A_sum = sum(A)
    ans = float("inf")
    for i in range(N + 1):
        s = A_sum
        if 0 < i <= N:
            s += L_cum_sum_min[i]
        if i < N:
            s += R_cum_sum_min[N - i]
        ans = min(ans, s)

    print(ans)


if __name__ == "__main__":
    main()
