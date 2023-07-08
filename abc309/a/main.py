def main():
    A, B = map(int, input().split())
    d = {
        1: (1, 1),
        2: (1, 2),
        3: (1, 3),
        4: (2, 1),
        5: (2, 2),
        6: (2, 3),
        7: (3, 1),
        8: (3, 2),
        9: (3, 3),
    }

    if d[A][0] == d[B][0] and abs(d[A][1] - d[B][1]) == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
