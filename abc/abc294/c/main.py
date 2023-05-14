def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result_a = []
    result_b = []
    limit = 10 ** 10
    a, b = limit, limit
    a_idx, b_idx = 0, 0
    for i in range(N+M):
        idx = str(i + 1)
        if a == limit and a_idx < len(A):
            a = A[a_idx]
            a_idx += 1
        if b == limit and b_idx < len(B):
            b = B[b_idx]
            b_idx += 1

        if a < b:
            result_a.append(idx)
            a = limit
        elif b < a:
            result_b.append(idx)
            b = limit

    print(" ".join(result_a))
    print(" ".join(result_b))


if __name__ == "__main__":
    main()