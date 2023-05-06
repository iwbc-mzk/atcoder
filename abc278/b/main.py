def main():
    H, M = input().split()
    H = H.zfill(2)
    M = M.zfill(2)

    while True:
        H2 = H[0] + M[0]
        M2 = H[1] + M[1]

        if 0 <= int(H2) <= 23 and 0 <= int(M2) <= 59:
            print(int(H), int(M))
            break

        if int(M) < 59:
            M = str(int(M)+1).zfill(2)
        elif int(M) == 59:
            M = "00"
            H = str(int(H)+1).zfill(2) if int(H) < 23 else "00"


if __name__ == "__main__":
    main()