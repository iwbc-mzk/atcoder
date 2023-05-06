def main():
    N = int(input())
    P = list(map(int, input().split()))

    n = -1
    for i in reversed(range(1, N)):
        if P[i-1] - P[i] > 0:
            n = i - 1
            break
    
    max_v = 0
    m = -1
    for j in range(n+1, N):
        if max_v < P[j] < P[n]:
            m = j
            max_v = P[j]

    P[n], P[m] = P[m], P[n]
    print(*P[:n+1], *P[:n:-1])


if __name__ == "__main__":
    main()
