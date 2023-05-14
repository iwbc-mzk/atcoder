def main():
    H, W = map(int, input().split())

    S = []
    for h in range(H):
        s = input()
        for i in range(len(s)):
            if i == len(s) - 1:
                break

            if s[i] == "T" and s[i+1] == "T":
                s = s[:i] + "PC" + s[i+2:]

        print(s)


if __name__ == "__main__":
    main()