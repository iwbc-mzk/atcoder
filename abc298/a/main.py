def main():
    N = int(input())
    S = input()
    
    ok = False
    ng = False
    for s in S:
        if s == "o":
            ok = True
        if s == "x":
            ng = True

    ans = "Yes" if ok and not ng else "No"
    print(ans)


if __name__ == "__main__":
    main()