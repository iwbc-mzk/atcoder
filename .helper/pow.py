def pow(x, n, mod=1):
    """
    xのn乗を計算する。
    pypy3(7.3.0)では組み込みのpow関数が実装されていないため暫定的に利用する
    """
    if n == 0:
        return 1
    elif n % 2:
        return (x * (pow(x, n - 1, mod) % mod)) % mod
    else:
        return ((pow(x, n // 2, mod) % mod) ** 2) % mod
