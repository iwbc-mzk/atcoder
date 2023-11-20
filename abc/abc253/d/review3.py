from math import lcm


def main():
    N, A, B = map(int, input().split())

    a_n = N // A
    b_n = N // B

    a_sum = a_n * A * (1 + a_n) // 2
    b_sum = b_n * B * (1 + b_n) // 2

    AB = lcm(A, B)
    ab_n = N // AB
    ab_sum = ab_n * AB * (1 + ab_n) // 2

    n_sum = N * (1 + N) // 2

    ans = n_sum - a_sum - b_sum + ab_sum
    print(ans)


if __name__ == "__main__":
    main()
