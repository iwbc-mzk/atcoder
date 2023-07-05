import math


def main():
    X, A, D, N = map(int, input().split())

    S = lambda x: A + (x - 1) * D

    if N == 1:
        print(abs(S(N) - X))
        return

    left = 1
    right = N
    d = 1 if D >= 0 else -1
    while right - left > 1:
        middle = (right + left) // 2
        s = S(middle)

        if d * s < d * X:
            left = middle
        else:
            right = middle

    ans = math.inf
    for i in range(2):
        ans = min(ans, abs(X - S(middle + i)), abs(X - S(middle - i)))

    print(ans)


if __name__ == "__main__":
    main()
