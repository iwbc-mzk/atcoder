import math


def rotate(
    angle_degree: float, x: float, y: float, cx: float = 0.0, cy: float = 0.0
):
    cosz = math.cos(math.radians(angle_degree))
    sinz = math.sin(math.radians(angle_degree))

    xx = (x - cx) * cosz - (y - cy) * sinz + cx
    yy = (y - cy) * cosz + (x - cx) * sinz + cy

    return xx, yy


def main():
    a, b, d = map(int, input().split())
    x, y = rotate(d, a, b)
    print(x, y)


if __name__ == "__main__":
    main()
