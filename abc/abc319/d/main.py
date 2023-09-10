def main():
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    left, right = 0, 10**15
    while right - left > 1:
        m = (left + right) // 2

        w = 0
        row = 0
        for i, l in enumerate(L):
            if i != 0 and w + l + 1 <= m:
                w += l + 1
            else:
                if l > m:
                    row = M + 1
                    break
                w = l
                row += 1

        if row <= M:
            right = m
        else:
            left = m

    print(right)


if __name__ == "__main__":
    main()
