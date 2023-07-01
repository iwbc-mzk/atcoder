def main():
    N, X = map(int, input().split())
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    i = X // N
    j = X % N
    if j == 0:
        i -= 1
    print(alpha[i])


if __name__ == "__main__":
    main()
