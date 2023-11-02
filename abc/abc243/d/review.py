def main():
    N, X = map(int, input().split())
    S = input()

    SS = []
    for s in S:
        if s != "U":
            SS.append(s)
        else:
            if SS and SS[-1] != "U":
                SS.pop()
            else:
                SS.append(s)

    ans = X
    for s in SS:
        if s == "U":
            ans //= 2
        elif s == "L":
            ans *= 2
        else:
            ans *= 2
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
