import sys

sys.setrecursionlimit(10**9)


def main():
    N, K, P = map(int, input().split())
    C, A = [], []
    S = [0] * K
    for _ in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
        for i, ai in enumerate(a):
            S[i] += ai

    ok = True
    for s in S:
        if s < P:
            ok = False
            break

    if not ok:
        print(-1)
        return

    ans = float("inf")

    def rec(i, c, v1, v2, v3, v4, v5):
        nonlocal ans

        if i == N:
            return

        cc = c + C[i]
        v = [v1, v2, v3, v4, v5]
        ok = True
        for j in range(K):
            v[j] += A[i][j]
            if v[j] < P:
                ok = False

        if ok:
            ans = min(ans, cc)
        else:
            rec(i + 1, cc, *v)

        rec(i + 1, c, v1, v2, v3, v4, v5)

    rec(0, 0, 0, 0, 0, 0, 0)
    print(ans)


if __name__ == "__main__":
    main()
