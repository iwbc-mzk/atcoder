from collections import defaultdict


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = defaultdict(int)
    right = 0
    l = 0
    ans = 0
    for left in range(N):
        if left > 0:
            a = A[left - 1]
            cnt[a] -= 1
            l -= 1
            if cnt[a] <= 0:
                del cnt[a]

        while True:
            if len(cnt.keys()) > K:
                right -= 1
                l -= 1
                cnt[A[right]] -= 1
                break

            if right == N:
                break

            l += 1
            cnt[A[right]] += 1
            right += 1

        ans = max(ans, l)

    print(ans)


if __name__ == "__main__":
    main()
