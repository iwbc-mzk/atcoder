def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))

    l = set()
    for i in range(N):
        a1 = A[i]
        if a1 <= W:
            l.add(a1)
        for j in range(N):
            if j == i:
                continue
            a2 = A[j]
            if a1 + a2 <= W:
                l.add(a1 + a2)
            for k in range(N):
                if k in [i, j]:
                    continue

                a3 = A[k]
                if a1 + a2 + a3 <= W:
                    l.add(a1 + a2 + a3)

    print(len(l))


if __name__ == "__main__":
    main()
