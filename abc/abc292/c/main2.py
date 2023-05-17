from collections import defaultdict


def main():
    N = int(input())

    cnt = defaultdict(int)
    for x in range(1, N):
        for y in range(1, N):
            if x * y < N:
                cnt[x * y] += 1
            else:
                break

    ans = 0
    for ab in range(1, N):
        cd = N - ab
        ans += cnt[ab] * cnt[cd]

    print(ans)


if __name__ == "__main__":
    main()
