def main():
    N = int(input())
    S = input()
    flg = False
    for s in S:
        if s == "|":
            flg = not flg
        
        if s == "*":
            print("in" if flg else "out")
            break


if __name__ == "__main__":
    main()