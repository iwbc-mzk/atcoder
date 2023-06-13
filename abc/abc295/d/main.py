from collections import defaultdict


def main():
    S = list(map(int, list(input())))
    N = len(S)

    P = [0 for _ in range(N + 1)]
    M = defaultdict(int)
    M[P[0]] += 1

    for i, s in enumerate(S, 1):
        P[i] = P[i - 1] ^ (1 << s)
        M[P[i]] += 1

    ans = 0
    for v in M.values():
        ans += v * (v - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
