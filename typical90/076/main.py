def main():
    N = int(input())
    A = list(map(int, input().split()))

    S = sum(A)
    AA = A * 2

    left, right = 0, 0
    s = 0
    while left < N:
        while s < S / 10:
            s += AA[right]
            right += 1

        if s == S / 10:
            print("Yes")
            return
        else:
            s -= AA[left]
            left += 1
    else:
        print("No")
        return


if __name__ == "__main__":
    main()
