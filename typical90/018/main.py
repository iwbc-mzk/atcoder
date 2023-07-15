from math import pi, cos, sin, atan2, sqrt


def main():
    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())

    for _ in range(Q):
        E = int(input())

        theta = 3 * pi / 2 - 2 * pi * E / T

        y = L / 2 * cos(theta)
        z = L / 2 * (1 + sin(theta))

        xx = sqrt(X**2 + (Y - y) ** 2)

        ans = atan2(z, xx) / (2 * pi) * 360
        print(ans)


if __name__ == "__main__":
    main()
