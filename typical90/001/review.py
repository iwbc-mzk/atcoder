def main():
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))
    AA = [A[0]]
    for i in range(N - 1):
        AA.append(A[i + 1] - A[i])

    AA.append(L - A[-1])

    l, r = 0, L
    while r - l > 1:
        m = (r + l) // 2
        c = 0
        t = 0
        for a in AA:
            if t >= m:
                c += 1
                t = 0

            t += a
        else:
            if t >= m:
                c += 1

        if c >= K + 1:
            l = m
        else:
            r = m

    print(l)


if __name__ == "__main__":
    main()
