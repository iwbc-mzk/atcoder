def main():
    S = list(map(int, input().split()))
    pre = 0
    for s in S:
        if s < pre:
            print("No")
            return
        if not (100 <= s <= 675):
            print("No")
            return
        if s % 25:
            print("No")
            return

        pre = s
    else:
        print("Yes")


if __name__ == "__main__":
    main()
