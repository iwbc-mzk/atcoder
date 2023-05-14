def main():
    N = int(input())

    A, B = 1, N
    C, D = 1, N
    for i in range(20):
        if A != B:
            b = (A + B) // 2
            print(f"? {A} {b} {1} {N}")
            T = int(input())
            if T == -1:
                exit()
            if b - A + 1 == T:
                A = b + 1
            else:
                B = b
        else:
            d = (C + D) // 2
            print(f"? {1} {N} {C} {d}")
            T = int(input())
            if T == -1:
                exit()
            if d- C + 1 == T:
                C = d + 1
            else:
                D = d
        if A == B and C == D:
            break
    
    print(f"! {A} {C}")


if __name__ == "__main__":
    main()