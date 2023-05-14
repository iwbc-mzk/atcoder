def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    indexes = {}
    for i, a in enumerate(A):
        indexes[a] = i
            
    idx = None
    for i in range(0, N):
        if idx:
            break

        for j in range(1, N+1):
            if K == 0:
                idx = (i, indexes[j])
                break

            if j == A[i]:
                d = (N - 1 - i) * (N - i) / 2 + 1
                if K - d <= 0:
                    break 
                K -= 1
            else:
                K -= 1

    # a, b, c =  A[:idx[0]], list(reversed(A[idx[0]:idx[1]+1])), A[idx[1]+1:]
    ans = A[:idx[0]] + list(reversed(A[idx[0]:idx[1] + 1])) + A[idx[1]+1:]
    print(*ans)

if __name__ == "__main__":
    main()