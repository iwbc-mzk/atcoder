def main():
    N = int(input())
    A = list(map(int, input().split()))
    sorted_A = sorted(A)

    idx = 0
    min_hp = sorted_A[0]
    while True:
        for j in range(N):
            if j == idx:
                continue

            v = sorted_A[j] % min_hp
            sorted_A[j] = v
            if 0 < v < min_hp:
                idx = j
                min_hp = v
                break
        else:
            print(min_hp)
            break


if __name__ == "__main__":
    main()