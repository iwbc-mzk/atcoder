def main():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())

        L = 0
        while N:
            L += N % 3
            N //= 3

        if L > K:
            print("No")
        elif L == K:
            print("Yes")
        else:
            if L % 2 == K % 2:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
