def mod_comb(n: int, k: int, mod: int, memo: list=None) -> int:
    """
    nCkの組み合わせをmodの基で計算する。

    Args:
        n (int): _description_
        k (int): _description_
        mod (int): _description_
        memo (list, optional): 1-indexedでの階乗メモ

    Returns:
        int: 計算結果
    """
    if not memo:
        memo = [1]
        for i in range(n + 1):
            memo.append((memo[i - 1] * i) % mod)

    def extGCD(a: int, b: int) -> tuple[int, int]:
        if b == 0:
            return (a, 1, 0)

        q, r = a // b, a % b
        y, x = extGCD(b, r)
        y -= q * x

        return (x, y)

    return memo[n] * extGCD(memo[n - k], mod)[0] * extGCD(memo[k], mod)[0]
