import bisect


def main():
    N, M, D = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    ans = -1
    for a in A:
        i = bisect.bisect_right(B, a + D) - 1
        if 0 <= i < len(B) and abs(B[i] - a) <= D:
            ans = max(ans, B[i] + a)

    print(ans)


if __name__ == "__main__":
    main()
