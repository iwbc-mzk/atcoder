from math import lcm


def main():
    N, A, B = map(int, input().split())

    if A > B:
        A, B = B, A

    if B % A:
        end_a = A * (N // A)
        end_b = B * (N // B)

        ab = lcm(*[A, B])
        end_ab = ab * (N // ab)

        total_n = (1 + N) * N // 2
        total_a = (A + end_a) * (N // A) // 2
        total_b = (B + end_b) * (N // B) // 2

        total_ab = (ab + end_ab) * (N // (ab)) // 2

        ans = total_n - total_a - total_b + total_ab
    else:
        end_a = A * (N // A)

        total_n = (1 + N) * N // 2
        total_a = (A + end_a) * (N // A) // 2

        ans = total_n - total_a

    print(ans)


if __name__ == "__main__":
    main()
