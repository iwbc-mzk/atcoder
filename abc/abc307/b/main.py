def main():
    N = int(input())
    S = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            s = S[i] + S[j]
            for k in range(len(s)):
                if s[k] != s[-1 - k]:
                    break
            else:
                print("Yes")
                return
    else:
        print("No")


if __name__ == "__main__":
    main()
