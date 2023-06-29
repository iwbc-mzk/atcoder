def main():
    N = int(input())
    A = list(map(int, input().split()))

    S = [0]
    for a in A:
        S.append(S[-1] + (1 if a else -1))

    min_s = 0
    max_s = 0
    up = 0
    lo = 0
    for s in S:
        up = max(up, s - min_s)
        lo = min(lo, s - max_s)

        min_s = min(min_s, s)
        max_s = max(max_s, s)

    print(up - lo + 1)


if __name__ == "__main__":
    main()
