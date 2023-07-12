def main():
    N = int(input())

    S = [[], [1]]
    for n in range(2, N + 1):
        s = S[n - 1] + [n] + S[n - 1]
        S.append(s)

    print(*S[N])


if __name__ == "__main__":
    main()
