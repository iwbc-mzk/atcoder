def main():
    N = int(input())
    S = set(input() for _ in range(N))

    if len(S) != N:
        print("No")
    else:
        for s in S:
            if s[0] not in ["H", "D", "C", "S"]:
                print("No")
                break

            if s[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
                print("No")
                break
        else:
            print("Yes")


if __name__ == "__main__":
    main()