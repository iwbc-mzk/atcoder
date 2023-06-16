import math


def main():
    N = int(input())
    sqrtN = math.sqrt(N)

    ans = 0
    i = 1
    while i <= sqrtN:
        v = N // i
        ans += v
        if i != N // i:
            ans += i * (N // i - N // (i + 1))
        i += 1

    print(ans)


if __name__ == "__main__":
    main()
