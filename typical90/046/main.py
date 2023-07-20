from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ad = defaultdict(int)
    bd = defaultdict(int)
    cd = defaultdict(int)

    for a, b, c in zip(A, B, C):
        ad[a % 46] += 1
        bd[b % 46] += 1
        cd[c % 46] += 1

    ans = 0
    for ai, av in ad.items():
        for bi, bv in bd.items():
            for ci, cv in cd.items():
                if (ai + bi + ci) % 46 == 0:
                    ans += av * bv * cv

    print(ans)


if __name__ == "__main__":
    main()
