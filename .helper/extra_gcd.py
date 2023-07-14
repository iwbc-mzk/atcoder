# ax + by = gcd(a, b) = d となる d, x, yを返す
def extGCD(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)

    d, y, x = extGCD(b, a % b)
    y -= (a // b) * x

    return (d, x, y)
