def main():
    N, A, B = map(int, input().split())
    S = input()

    S += S # ABC => ABCABC
    min_price = 1 << 60
    for i in range(N):
        price = A * i
        for j in range(N//2):
            if S[i+j] != S[N-1+i-j]:
                price += B

        min_price = min(min_price, price)

    print(min_price)


if __name__ == "__main__":
    main()