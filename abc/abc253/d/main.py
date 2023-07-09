from math import gcd


def main():
    N, A, B = map(int, input().split())

    total = N * (1 + N) // 2

    cnt_A = N // A
    total_A = cnt_A * (2 * A + (cnt_A - 1) * A) // 2

    if A != B:
        cnt_B = N // B
        total_B = cnt_B * (2 * B + (cnt_B - 1) * B) // 2

        AB = A * B // gcd(A, B)
        cnt_AB = N // AB
        total_AB = cnt_AB * (2 * AB + (cnt_AB - 1) * AB) // 2

        ans = total - total_A - total_B + total_AB
    else:
        ans = total - total_A

    print(ans)


if __name__ == "__main__":
    main()
