def main():
    X, Y, Z = map(int, input().split())
    start = 0

    if X < Y < start or start < Y < X:
        if Z < Y < start or start < Y < Z:
            print(-1)
        else:
            print(abs(Z - start) + abs(X - Z))
    else:
        print(abs(X - start))



if __name__ == "__main__":
    main()