def main():
    N = int(input())
    S = input()

    if "-" in S:
        SS = S.split("-")
        ans = -1
        for s in SS:
            if not s:
                continue
            ans = max(ans, len(s))

        print(ans)
    else:
        print(-1)



if __name__ == "__main__":
    main()