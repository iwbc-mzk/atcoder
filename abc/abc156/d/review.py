# 参考: https://drken1215.hatenablog.com/entry/2018/06/08/210000
def mod_comb(n: int, k: int, mod: int, memo: list = None) -> int:
    """
    nCkの組み合わせをmodの基で計算する。
    計算量:
        引数にてmemoを渡した場合 O(1)
        渡さない場合は O(k)

    Args:
        n (int): _description_
        k (int): _description_
        mod (int): _description_
        memo (list, optional): 1-indexedでの階乗メモ

    Returns:
        int: 計算結果
    """

    def extGCD(a: int, b: int) -> tuple[int, int]:
        if b == 0:
            return (1, 0)

        q, r = a // b, a % b
        y, x = extGCD(b, r)
        y -= q * x

        return (x, y)

    if memo:
        return memo[n] * extGCD(memo[n - k], mod)[0] * extGCD(memo[k], mod)[0]
    else:
        k = min(k, n - k)

        comb1 = 1
        for v in range(n - k + 1, n + 1):
            comb1 = (comb1 * v) % mod

        comb2 = 1
        for v in range(1, k + 1):
            comb2 = (comb2 * v) % mod

        return comb1 * extGCD(comb2, mod)[0]


def main():
    N, A, B = map(int, input().split())
    MOD = 10**9 + 7

    total = pow(2, N, MOD) - 1
    a_n = mod_comb(N, A, MOD)
    b_n = mod_comb(N, B, MOD)

    print((total - a_n - b_n) % MOD)


if __name__ == "__main__":
    main()
