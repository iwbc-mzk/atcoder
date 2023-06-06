def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_sum = [0]
    for i, a in enumerate(A, 1):
        s = A_sum[i - 1] + a
        A_sum.append(s)

    B_sum = [0]
    for i, b in enumerate(B, 1):
        s = B_sum[i - 1] + b
        B_sum.append(s)

    # 尺取り法
    ans = 0
    i_b = M
    for i_a, a_sum in enumerate(A_sum):
        while a_sum + B_sum[i_b] > K and i_b >= 0:
            i_b -= 1
        else:
            if i_b >= 0:
                ans = max(ans, i_a + i_b)

    print(ans)


if __name__ == "__main__":
    main()
