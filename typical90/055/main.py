from itertools import combinations


def main():
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        ti = A[i] % P
        for j in range(i + 1, N):
            tj = ti * A[j] % P
            for k in range(j + 1, N):
                tk = tj * A[k] % P
                for l in range(k + 1, N):
                    tl = tk * A[l] % P
                    for m in range(l + 1, N):
                        t = tl * A[m] % P
                        t %= P
                        if t == Q:
                            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
