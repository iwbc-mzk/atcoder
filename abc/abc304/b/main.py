def main():
    N = float(input())
    if N <= 10**3 - 1:
        print(int(N))
    elif 10**3 <= N <= 10**4 - 1:
        print(int(N // 10 * 10))
    elif 10**4 <= N <= 10**5 - 1:
        print(int(N // 100 * 100))
    elif 10**5 <= N <= 10**6 - 1:
        print(int(N // 1000 * 1000))
    elif 10**6 <= N <= 10**7 - 1:
        print(int(N // 10000 * 10000))
    elif 10**7 <= N <= 10**8 - 1:
        print(int(N // 100000 * 100000))
    elif 10**8 <= N <= 10**9 - 1:
        print(int(N // 1000000 * 1000000))


if __name__ == "__main__":
    main()
