import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


# ランレングス圧縮
def run_length_encoding(s):
    pre = s[0]
    cnt = 0
    result = []
    for si in s:
        if si == pre:
            cnt += 1
        else:
            result.append((pre, cnt))
            pre = si
            cnt = 1
    else:
        result.append((pre, cnt))

    return result


from typing import List, Union, TypeVar, Optional, Callable
from math import gcd

T = TypeVar("T")


# 参考: https://algo-logic.info/segment-tree/
class SegTree:
    def __init__(
        self,
        init: Union[List[T], int],
        type_: str = "min",
        segfunc: Optional[Callable[[T, T], T]] = None,
        init_val: Optional[T] = None,
    ) -> None:
        """
        初期化処理

        Args:
            init_list (List[T]): セグメント木として管理するリスト
            type_ (str, optional): セグメント木のタイプ
                                   利用可能なのは"min", "max", "sum", "product", "gcd", "original"
                                   デフォルトは"min"
                                   "original"指定時はsegfuncとinit_valの指定も必要
            segfunc (Optional[Callable[[T, T], T]], optional): 各区間に行いたい処理
                                                                     type_で"original"指定時のみ有効
            init_val (Optional[T], optional): 各区間の初期値
                                                type_で"original"指定時のみ有効

        Raises:
            ValueError: 無効なtype_を指定時
        """
        n: int = len(init) - 1 if type(init) == list else init - 1
        self._n = 1 << n.bit_length()

        if type_ == "min":
            self._segfunc = min
            self._init_val = 10**18
        elif type_ == "max":
            self._segfunc = max
            self._init_val = -(10**18)
        elif type_ == "sum":
            self._segfunc = sum
            self._init_val = 0
        elif type_ == "product":
            self._segfunc = lambda x, y: x * y
            self._init_val = 1
        elif type_ == "gcd":
            self._segfunc = gcd
            self._init_val = 0
        elif type_ == "original":
            self._segfunc = segfunc
            self._init_val = init_val
        else:
            raise ValueError()

        self._tree = [self._init_val] * (2 * self._n - 1)

        if type(init) == list:
            # x個の初期値(葉)は self._n - 1 ~ x + self._n - 1 に格納される
            # ノードは 0 ~ self._n - 2
            self._tree[self._n - 1 : self._n - 1 + len(init)] = init
            for i in range(self._n - 2, -1, -1):
                self._update(i)

    def __repr__(self) -> str:
        l, r = 1, 2
        res = []
        while r <= 2 * self._n:
            res.append(f"{self._tree[l:r]}")
            l, r = r, r << 1

        return "\n".join(res)

    def update(self, i: int, x: T) -> None:
        """
        数列の値の更新を行う
        計算量 O(logN)

        Args:
            i (int): 更新したい数列の位置
            x (T): 更新する値
        """
        # 数列のi番目の値はself._tree上ではn-1+i番目に格納されている
        i += self._n - 1
        self._tree[i] = x

        # 親の更新
        while i > 0:
            # 親ノードの位置
            i = (i - 1) // 2
            self._update(i)

    def _update(self, i: int) -> None:
        # 親ノードの位置がiの時、子ノードは 2i+1, 2i+2 になる
        self._tree[i] = self._segfunc([self._tree[i * 2 + 1], self._tree[i * 2 + 2]])

    def query(self, a: int, b: int) -> T:
        """
        区間 [a, b) で segfuncを実行した結果を返す
        計算量 O(logN)

        Args:
            a (int): 区間の最初のインデックス(区間に含む)
            b (int): 区間の最後のインデックス(区間に含まない)

        Returns:
            T: 区間 [a, b) の最小値
        """
        l = max(a, 0) + self._n
        r = min(b, self._n) + self._n
        v = self._init_val
        while l < r:
            if l & 1:
                v = self._segfunc([v, self._tree[l - 1]])
                l += 1
            if r & 1:
                r -= 1
                v = self._segfunc([v, self._tree[r - 1]])

            l >>= 1
            r >>= 1

        return v


def main():
    N = int(input())
    A = list(map(int, input().split()))

    AA = run_length_encoding(A)

    D = defaultdict(list)
    C = []

    for i, a in enumerate(AA):
        v = a[0]
        D[v].append(i)
        C.append(a[1])

    seg = SegTree(init=C, type_="sum")

    ans = 0
    for key, val in D.items():
        for i in range(len(val)):
            for j in range(i + 1, len(val)):
                l, r = val[i], val[j]
                if r - l > 1:
                    ans += seg.query(l + 1, r) * C[l] * C[r]

    print(ans)


if __name__ == "__main__":
    main()
