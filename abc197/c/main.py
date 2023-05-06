def main():
    N = int(input())
    A = list(map(int, input().split()))

    result = 10 ** 10
    for s in range(2 ** (N-1)):
        ored = 0
        xored = 0
        for n in range(N-1):
            ored |= A[n]
            if s >> n & 1:
                xored ^= ored
                ored = 0
        else:
            xored ^= (ored | A[N-1])

        result = min(result, xored)
    return result

print(main())