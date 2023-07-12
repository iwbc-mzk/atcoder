def main():
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))

    A = [0] + A + [L]

    left = -1
    right = L + 1
    while right - left > 1:
        mid = (right + left) // 2

        l = 0
        k = 0
        for i in range(1, len(A)):
            l += A[i] - A[i - 1]
            if l >= mid:
                k += 1
                l = 0

        if k >= K + 1:
            left = mid
        else:
            right = mid

    print(left)


if __name__ == "__main__":
    main()
