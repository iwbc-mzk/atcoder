def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        S = input()

        for i in range(1, N):
            left = S[:i]
            right = S[i:]
            if left < right:
                print("Yes")
                break
        else:
            print("No")


if __name__ == "__main__":
    main()
