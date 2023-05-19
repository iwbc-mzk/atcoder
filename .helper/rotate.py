import math


def rotate(
    radian: float, x: float, y: float, cx: float = 0.0, cy: float = 0.0
) -> tuple[float, float]:
    cosz = math.cos(math.radians(radian))
    sinz = math.sin(math.radians(radian))

    xx = (x - cx) * cosz - (y - cy) * sinz + cx
    yy = (y - cy) * cosz + (x - cx) * sinz + cy

    return xx, yy
