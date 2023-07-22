def main():
    N = int(input())
    S = input()
    c = [0, 0, 0]
    for i, si in enumerate(S, 1):
        if si == "A":
            c[0] += 1
        elif si == "B":
            c[1] += 1
        elif si == "C":
            c[2] += 1

        for j in c:
            if j == 0:
                break
        else:
            print(i)
            return


if __name__ == "__main__":
    main()
