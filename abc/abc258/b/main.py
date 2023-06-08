def main():
    N = int(input())
    A = [list(map(int, list(input()))) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            for dx in [0, 1, -1]:
                for dy in [0, 1, -1]:
                    if not dx and not dy:
                        continue

                    v = 0
                    for n in range(N):
                        x = (i + dx * n) % N
                        y = (j + dy * n) % N
                        v += A[x][y] * 10**n
                    else:
                        ans = max(ans, v)

    print(ans)


if __name__ == "__main__":
    main()
