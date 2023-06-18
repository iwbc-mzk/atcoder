def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))

        ans = 0
        for i in range(N):
            pi = P[i]
            if i + 1 < pi:
                continue

            for j in range(i + 1, N):
                pj = P[j]
                if pi > pj:
                    break
            else:
                ans += 1

        print(ans)


if __name__ == "__main__":
    main()
