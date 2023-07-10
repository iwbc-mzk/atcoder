from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))

    D = defaultdict(int)
    for a in A:
        D[a] += 1

    AS = set(A)
    A = list(AS)
    A.sort()

    M = max(A)

    ans = 0
    for q in A:
        for r in A:
            if r > M / q:
                break

            if q * r in AS:
                ans += D[q] * D[r] * D[q * r]

    print(ans)


if __name__ == "__main__":
    main()
