import bisect


def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_sum = [0]
    for i, a in enumerate(A, 1):
        s = A_sum[i - 1] + a
        if s <= K:
            A_sum.append(s)
        else:
            break

    B_sum = [0]
    for i, b in enumerate(B, 1):
        s = B_sum[i - 1] + b
        B_sum.append(s)

    ans = 0
    for a_cnt, a_sum in enumerate(A_sum):
        remain_time = K - a_sum
        b_cnt = bisect.bisect_right(B_sum, remain_time) - 1

        ans = max(ans, a_cnt + b_cnt)

    print(ans)


if __name__ == "__main__":
    main()
