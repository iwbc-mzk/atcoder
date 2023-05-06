def main():
    X, Y, N = map(int, input().split())
    
    ans = 0
    if float(X) < Y / 3:
        ans = X * N
    else:
        remain = N
        while remain >= 3:
            ans += Y
            remain -= 3

        ans += X * remain

    print(ans)

if __name__ == "__main__":
    main()