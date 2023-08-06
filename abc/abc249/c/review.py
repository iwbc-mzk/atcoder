from collections import defaultdict


def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    D = []
    for s in S:
        d = defaultdict(int)
        for si in s:
            d[si] += 1

        D.append(d)

    ans = 0
    for i in range(2**N + 1):
        cnt = defaultdict(int)
        for j in range(N):
            if i >> j & 1:
                s = D[j]
                for k in range(26):
                    alp = chr(ord("a") + k)
                    if alp in s:
                        cnt[alp] += 1

        a = 0
        for v in cnt.values():
            if v == K:
                a += 1
        ans = max(ans, a)

    print(ans)


if __name__ == "__main__":
    main()
