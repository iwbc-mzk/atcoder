def main():
    N = int(input())
    if N % 5 <= 2:
        print(N - N % 5)
    else:
        print(N + (5 - N % 5))


if __name__ == "__main__":
    main()
