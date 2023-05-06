def main():
    N, X = map(int, input().split())
    A = set(map(int, input().split()))

    for a in A:
        if a + X in A:
            print("Yes")
            break
    else:
        print("No")

if __name__ == "__main__":
    main()