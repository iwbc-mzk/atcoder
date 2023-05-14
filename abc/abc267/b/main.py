def main():
    S = input()

    columns = set()
    for i, s in enumerate(S, 1):
        if s == "1":
            if i == 7:
                columns.add(1)
            if i == 4:
                columns.add(2)
            if i in [2, 8]:
                columns.add(3)
            if i in [1, 5]:
                columns.add(4)
            if i in [3, 9]:
                columns.add(5)
            if i == 6:
                columns.add(6)
            if i == 10:
                columns.add(7)
    
    ans = S[0] == "0"
    if len(columns):
        max_columns = max(columns)
        min_columns = min(columns)
        if max_columns - min_columns + 1 != len(columns):
            ans &= True
        else:
            ans &= False
    else:
        ans = False

    print("Yes" if ans else "No")


if __name__ == "__main__":
    main()