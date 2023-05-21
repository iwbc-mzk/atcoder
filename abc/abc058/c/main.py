from collections import defaultdict


def main():
    N = int(input())
    S = [input() for _ in range(N)]

    D = []
    for s in S:
        d = defaultdict(int)
        for si in s:
            d[si] += 1
        D.append(d)

    m = D[0]
    for i in range(1, N):
        d1 = m
        d2 = D[i]
        d = defaultdict(int)
        for key in d1.keys():
            d[key] = min(d1[key], d2[key])

        m = d

    ans = []
    for key in sorted(d.keys()):
        val = m[key]
        for _ in range(val):
            ans.append(key)

    print("".join(ans))


if __name__ == "__main__":
    main()
