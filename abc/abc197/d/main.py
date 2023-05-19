import math


def rotate(
    radian: float, x: float, y: float, cx: float = 0.0, cy: float = 0.0
) -> tuple[float, float]:
    cosz = math.cos(math.radians(radian))
    sinz = math.sin(math.radians(radian))

    xx = (x - cx) * cosz - (y - cy) * sinz + cx
    yy = (y - cy) * cosz + (x - cx) * sinz + cy

    return xx, yy


def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xn2, yn2 = map(int, input().split())

    cx, cy = (x0 + xn2) / 2, (y0 + yn2) / 2

    print(*rotate(360 /N, x0, y0, cx, cy))


if __name__ == "__main__":
    main()
