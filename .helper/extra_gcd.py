# ax + by = gcd(a, b) = d となる d, x, yを返す
# mod P でのkの逆元計算はextGCD(P, k)のyになる
def extGCD(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)

    # a = qb + r => rx + b(qx + y) = d
    q, r = a // b, a % b
    d, y, x = extGCD(b, r)
    y -= q * x

    return (d, x, y)


if __name__ == "__main__":
    # mod 61 での25の逆元は 22
    print(extGCD(61, 25))  # 22
