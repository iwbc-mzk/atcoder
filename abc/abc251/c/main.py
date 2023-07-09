def main():
    N = int(input())

    ST = []
    l = set()
    for i in range(N):
        S, T = input().split()
        T = int(T)

        original = S not in l
        ST.append((-T, S, i, original))
        l.add(S)

    ST.sort()
    for t, s, i, original in ST:
        if original:
            print(i + 1)
            return


if __name__ == "__main__":
    main()
