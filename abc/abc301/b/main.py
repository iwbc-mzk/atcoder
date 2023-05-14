def main():
    N = int(input())
    A = list(map(int, input().split()))

    l = []
    for i in range(N - 1):
        ai = A[i]
        aj = A[i + 1]

        l.append(ai)
        if abs(ai - aj) == 1:
            continue
        
        if ai < aj:
            l += list(range(ai + 1, aj))
        else:
            l += list(reversed(range(aj + 1, ai)))

    l.append(A[-1])

    print(*l)

if __name__ == "__main__":
    main()