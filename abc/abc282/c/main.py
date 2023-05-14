def main():
    N = int(input())
    S = list(input())

    inner = False
    l = []
    for i, s in enumerate(S):
        if s == '"':
            inner = not inner

        if s == ",":
            if not inner:
                l.append(i)

    for i in l:
        S[i] = "."

    print("".join(S))


if __name__ == "__main__":
    main()