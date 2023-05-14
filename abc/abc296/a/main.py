def main():
    N = int(input())
    S = input()

    pre = ""
    for s in S:
        if pre and s == pre:
            print("No")
            break
        pre = s
            
    else:
        print("Yes")


if __name__ == "__main__":
    main()