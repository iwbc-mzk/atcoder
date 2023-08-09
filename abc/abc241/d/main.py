from typing import Union, TypeVar

T = TypeVar("T")


# https://scrapbox.io/pocala-kyopro/BIT
# https://qiita.com/toast-uz/items/bf6f142bace86c525532#13-bit
# https://qiita.com/u2dayo/items/092fcdfb7902db6a9a72#d%E5%95%8F%E9%A1%8Csequence-query
class BIT:
    """
    Binary Indexed Tree (Fenwick tree)
    1点加算と閉区間[1, i]の和の取得を高速計量(それぞれO(logN))に実行できる
    """

    def __init__(self, n: Union[list, int]) -> None:
        self._n = len(n) if isinstance(n, list) else n
        self._size = 1 << (self._n - 1).bit_length()

        if isinstance(n, list):
            a = [0]
            for p in n:
                a.append(p + a[-1])
            a += [a[-1]] * (self._size - self._n)
            self._data = [a[p] - a[p - (p & -p)] for p in range(self._size + 1)]
        else:
            self._data = [0] * (self._size + 1)

    def __len__(self):
        return self._n

    def add(self, i: int, x: int) -> None:
        while i <= self._size:
            self._data[i] += x
            i += i & -i

    def get(self, i: int) -> int:
        return self.sum_range(i, i - 1)

    def sum(self, i: int) -> int:
        """
        区間[0, i]の総和

        Args:
            i (int): _description_

        Returns:
            int: _description_
        """
        s = 0
        while i > 0:
            s += self._data[i]
            i -= i & -i

        return s

    def sum_range(self, l: int, r: int) -> int:
        """
        区間[l, r]の総和

        Args:
            l (int): _description_
            r (int): _description_

        Returns:
            int: _description_
        """
        return self.sum(r) - self.sum(l - 1)

    def lower_bound(self, lower: int) -> int:
        """
        lower <= 閉区間[1, x]の累積和 となる最小のxを返す

        Args:
            lower (int): _description_

        Returns:
            int: lower <= 閉区間[1, x]の累積和 となる最小のx
        """
        if lower < 0:
            return 0

        x, r = 0, self._size
        while r > 0:
            if x + r <= self._n and self._data[x + r] < lower:
                lower -= self._data[x + r]
                x += r
            r //= 2

        return x + 1


def main():
    Q = int(input())

    A = []
    query = []
    for _ in range(Q):
        i, *xk = map(int, input().split())

        if i == 1:
            x = xk[0]
        else:
            x, _ = xk
        A.append(x)
        query.append((i, xk))

    AA = sorted(set(A))
    D = {k: i for i, k in enumerate(AA, 1)}
    D_inv = {i: k for i, k in enumerate(AA, 1)}

    bit = BIT(len(D) + 1)
    for i, xk in query:
        if i == 1:
            x = xk[0]
            bit.add(D[x], 1)
        elif i == 2:
            x, k = xk
            c = bit.sum(D[x])
            t = c - k + 1
            if t > 0:
                v = bit.lower_bound(t)
                print(D_inv[v])
            else:
                print(-1)
        else:
            x, k = xk
            t = bit.sum_range(D[x], len(bit))
            if t >= k:
                c = bit.sum(D[x] - 1)
                t = c + k
                v = bit.lower_bound(t)
                print(D_inv[v])
            else:
                print(-1)


if __name__ == "__main__":
    main()
