# 算術級数(等差数列の和)
def arithmetic_series(n: int, v1: int, v2: int, with_common_diff=True):
    if with_common_diff:
        return n * (2 * v1 + (n - 1) * v2) // 2
    else:
        return n * (v1 + v2) // 2
