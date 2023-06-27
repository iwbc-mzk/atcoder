import bisect


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    BC = [tuple(map(int, input().split())) for _ in range(M)]
    BC.sort(key=lambda x: (x[1], x[0]), reverse=True)

    ans = 0
    last_idx = 0
    for B, C in BC:
        i = bisect.bisect_left(A, C, last_idx)
        if i <= last_idx:
            continue

        cnt = min(B, i - last_idx)
        ans += C * cnt
        last_idx += cnt

    ans += sum(A[last_idx:])

    print(ans)


if __name__ == "__main__":
    main()
