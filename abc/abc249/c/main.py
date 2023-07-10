from collections import defaultdict


def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    D = {}
    for s in S:
        d = defaultdict(int)
        for si in s:
            d[si] += 1

        D[s] = d

    ans = 0
    for i in range(2**N):
        cnt = defaultdict(int)
        for j in range(N):
            if i >> j & 1:
                for k in range(len(S[j])):
                    cnt[S[j][k]] += 1

        c = 0
        for v in cnt.values():
            if v == K:
                c += 1

        ans = max(ans, c)

    print(ans)


if __name__ == "__main__":
    main()
