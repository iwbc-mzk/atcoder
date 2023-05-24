import math

def main():
    X, Y, A, B = map(int, input().split())

    ans = 0
    x = math.log(min(B, Y) / X) // math.log(A)
    if x > 0:
        ans += x

    Y -= X * A ** (x if x > 0 else 0)
    ans += Y // B - (0 if Y % B else 1)

    print(int(ans))

if __name__ == "__main__":
    main()
