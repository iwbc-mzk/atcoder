from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))

    max_a = max(A)
    cnt = [0 for _ in range(max_a + 1)]
    for a in A:
        cnt[a] += 1

    for i in range(max_a):
        cnt[i + 1] += cnt[i]

    ans = 0
    for j in range(0, N):
        aj = A[j]
        i_cnt = cnt[aj - 1]
        k_cnt = cnt[max_a] - cnt[aj]
        ans += i_cnt * k_cnt

    print(ans)


if __name__ == "__main__":
    main()
