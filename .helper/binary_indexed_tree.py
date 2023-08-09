from typing import Union, TypeVar

T = TypeVar("T")


# https://scrapbox.io/pocala-kyopro/BIT
# https://qiita.com/toast-uz/items/bf6f142bace86c525532#13-bit
# https://qiita.com/u2dayo/items/092fcdfb7902db6a9a72#d%E5%95%8F%E9%A1%8Csequence-query
class BIT:
    """
    Binary Indexed Tree (Fenwick tree)
    1点加算と閉区間[1, i]の和の取得を高速計量(それぞれO(logN))に実行できる
    1-indexed(添え字が1から始まる)で実装
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
        """
        位置iにxを加算する

        Args:
            i (int): 位置インデックス
            x (int): 加算値
        """
        while i <= self._size:
            self._data[i] += x
            i += i & -i

    def get(self, i: int) -> int:
        return self.sum_range(i, i - 1)

    def sum(self, i: int) -> int:
        """
        閉区間[1, i]の総和

        Args:
            i (int): 閉区間の右インデックス

        Returns:
            int: 閉区間[1, i]の総和
        """
        s = 0
        while i > 0:
            s += self._data[i]
            i -= i & -i

        return s

    def sum_range(self, l: int, r: int) -> int:
        """
        閉区間[l, r]の総和

        Args:
            l (int): 閉区間の左インデックス
            r (int): 閉区間の右インデックス

        Returns:
            int: 閉区間[l, r]の総和
        """
        return self.sum(r) - self.sum(l - 1)

    def lower_bound(self, lower: int) -> int:
        """
        lower <= 閉区間[1, x]の累積和 となる最小のxを返す

        Args:
            lower (int): 累積和の下限値

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
