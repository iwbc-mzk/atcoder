def main():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {a: i+1 for i, a in enumerate(list(alpha))}

    S = input()

    length = len(S)
    result = 0
    for i in range(length):
        l = length - i - 1
        result += d[S[i]] * 26**l

    print(result)

if __name__ == "__main__":
    main()