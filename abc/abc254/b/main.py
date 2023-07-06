def main():
    N = int(input())

    A = []
    for i in range(N):
        Ai = [0 for _ in range(i + 1)]
        for j in range(len(Ai)):
            if j == 0 or j == i:
                Ai[j] = 1
            else:
                Ai[j] = A[i - 1][j - 1] + A[i - 1][j]
        A.append(Ai)

    for a in A:
        print(*a)


if __name__ == "__main__":
    main()
