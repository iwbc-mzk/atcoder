# ax + by = gcd(a, b) = d となる x, y, dを返す
# mod P でのkの逆元計算はextGCD(k, P)のxになる
def extGCD(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (1, 0, a)

    # a = qb + r => rx + b(qx + y) = d
    q, r = a // b, a % b
    y, x, d = extGCD(b, r)
    y -= q * x

    return (x, y, d)


if __name__ == "__main__":
    # mod 61 での25の逆元は 22
    print(extGCD(25, 61))  # (22, -9, 1)
