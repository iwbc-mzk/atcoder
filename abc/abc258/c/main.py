def main():
    N, Q = map(int, input().split())
    S = input()

    c = 0
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            c += x
        else:
            print(S[x - c % len(S) - 1])


if __name__ == "__main__":
    main()
