def main():
    S = input()

    if len(S) != 8:
        print("No")
    else:
        for i, s in enumerate(S):
            if i == 0 or i == len(S) - 1:
                # A~Z
                if 65 <= ord(s) <= 90:
                    continue
            
            if i == 1:
                # 1~9
                if 49 <= ord(s) <= 57:
                    continue
            
            if 2 <= i <= len(S) -2:
                # 0~9
                if 48 <= ord(s) <= 57:
                    continue

            print("No")
            break
        else:
            print("Yes")


if __name__ == "__main__":
    main()