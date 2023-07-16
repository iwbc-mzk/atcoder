def main():
    N = int(input())

    s = set()
    for i in range(1, N + 1):
        S = input()
        if S not in s:
            print(i)
            s.add(S)


if __name__ == "__main__":
    main()
