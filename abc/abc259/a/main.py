def main():
    N, M, X, T, D = map(int, input().split())

    if M >= X:
        print(T)
    else:
        print(T - D * (X - M))


if __name__ == "__main__":
    main()
