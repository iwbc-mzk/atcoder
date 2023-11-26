import sys

sys.setrecursionlimit(10**9)


def main():
    N, T = input().split()
    N = int(N)
    S = [input() for _ in range(N)]

    C = [[0, 0] for _ in range(N)]
    F = [0 for _ in range(len(T) + 1)]
    B = [0 for _ in range(len(T) + 1)]
    for i, s in enumerate(S):
        # 前から
        si, ti = 0, 0
        while si < len(s) and ti < len(T):
            if s[si] == T[ti]:
                ti += 1
            si += 1
        C[i][0] = max(ti, 0)
        F[max(ti, 0)] += 1

        # 後ろから
        si, ti = len(s) - 1, len(T) - 1
        while si >= 0 and ti >= 0:
            if s[si] == T[ti]:
                ti -= 1
            si -= 1
        C[i][1] = max(0, len(T) - ti - 1)
        B[max(0, len(T) - ti - 1)] += 1

    BB = []
    for b in B:
        if not BB:
            BB.append(b)
        else:
            BB.append(BB[-1] + b)

    ans = 0
    for i, s in enumerate(S):
        f = C[i][0]
        n = len(T) - f
        if n <= 0:
            ans += N
        else:
            ans += BB[-1] - BB[n - 1]

    print(ans)


if __name__ == "__main__":
    main()
