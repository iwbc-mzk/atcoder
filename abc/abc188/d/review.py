def main():
    N, c = map(int, input().split())

    A, B, C = [], [], []
    AB = set()
    max_b = 0
    for _ in range(N):
        a, b, c_ = map(int, input().split())
        C.append(c_)
        A.append(a)
        B.append(b + 1)
        AB.add(a)
        AB.add(b + 1)
        max_b = max(max_b, b + 1)

    AB.add(0)
    AB.add(max_b + 1)

    AB = sorted(AB)
    D = {key: i for i, key in enumerate(AB)}
    D_inv = {i: key for i, key in enumerate(AB)}
    AA, BB = [], []
    m = 0
    for a, b in zip(A, B):
        AA.append(D[a])
        BB.append(D[b])
        m = max(m, D[b])

    L = [0] * (m + 1)
    for a, b, c_ in zip(AA, BB, C):
        L[a] += c_
        L[b] += -c_

    ans = 0
    for i in range(len(L)):
        if i > 0:
            L[i] += L[i - 1]
        if i + 1 < len(L):
            ans += min(L[i], c) * (D_inv[i + 1] - D_inv[i])

    print(ans)


if __name__ == "__main__":
    main()
