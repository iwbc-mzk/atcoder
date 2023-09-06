from collections import defaultdict


def main():
    S = input()

    D = defaultdict(int)
    D[0] += 1
    d = 0
    for s in S:
        i = int(s)
        d = d ^ (1 << i)
        D[d] += 1

    ans = 0
    for v in D.values():
        ans += v * (v - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
