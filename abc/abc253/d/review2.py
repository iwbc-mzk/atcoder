from math import lcm


def main():
    N, A, B = map(int, input().split())

    AB = lcm(A, B)

    cnt_a = N // A
    cnt_b = N // B
    cnt_ab = N // AB

    sum_n = N * (N + 1) // 2
    sum_a = cnt_a * (2 * A + A * (cnt_a - 1)) // 2
    sum_b = cnt_b * (2 * B + B * (cnt_b - 1)) // 2
    sum_ab = cnt_ab * (2 * AB + AB * (cnt_ab - 1)) // 2

    print(sum_n - sum_a - sum_b + sum_ab)


if __name__ == "__main__":
    main()
