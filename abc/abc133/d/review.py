def main():
    N = int(input())
    A = list(map(int, input().split()))

    total = sum(A)
    x1 = total
    for i in range(N):
        if i % 2:
            x1 -= 2 * A[i]

    ans = [x1]
    for a in A[:-1]:
        ans.append((a - ans[-1] // 2) * 2)

    print(*ans)


if __name__ == "__main__":
    main()
