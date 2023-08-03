from typing import List, Union, TypeVar, Optional, Callable
from math import gcd

T = TypeVar("T")
Num = Union[int, float]


# 参考: https://algo-logic.info/segment-tree/
class SegTree:
    def __init__(
        self,
        init_list: List[Num],
        type_: str = "min",
        segfunc: Optional[Callable[[Num, Num], Num]] = None,
        init_val: Optional[Num] = None,
    ) -> None:
        """
        初期化処理

        Args:
            init_list (List[Num]): セグメント木として管理するリスト
            type_ (str, optional): セグメント木のタイプ
                                   利用可能なのは"min", "max", "sum", "product", "gcd", "original"
                                   デフォルトは"min"
                                   "original"指定時はsegfuncとinit_valの指定も必要
            segfunc (Optional[Callable[[Num, Num], Num]], optional): 各区間に行いたい処理
                                                                     type_で"original"指定時のみ有効
            init_val (Optional[Num], optional): 各区間の初期値
                                                type_で"original"指定時のみ有効

        Raises:
            ValueError: 無効なtype_を指定時
        """
        self._n = 1 << (len(init_list) - 1).bit_length()

        if type_ == "min":
            self._segfunc = lambda x, y: min(x, y)
            self._init_val = float("inf")
        elif type_ == "max":
            self._segfunc = lambda x, y: max(x, y)
            self._init_val = -float("inf")
        elif type_ == "sum":
            self._segfunc = lambda x, y: x + y
            self._init_val = 0
        elif type_ == "product":
            self._segfunc = lambda x, y: x * y
            self._init_val = 1
        elif type_ == "gcd":
            self._segfunc = lambda x, y: gcd(x, y)
            self._init_val = 0
        elif type_ == "original":
            self._segfunc = segfunc
            self._init_val = init_val
        else:
            raise ValueError()

        self._tree = [self._init_val] * 2 * self._n

        for i, v in enumerate(init_list):
            self.update(i, v)

    def update(self, i: int, x: int) -> None:
        """
        数列の値の更新を行う
        計算量 O(logN)

        Args:
            i (int): 更新したい数列の位置
            x (int): 更新する値
        """
        # 数列のi番目の値はself._tree上ではn-1+i番目に格納されている
        i += self._n - 1
        self._tree[i] = x

        # 親の更新
        while i > 0:
            # 親ノードの位置
            i = (i - 1) // 2
            # 親ノードの位置がiの時、子ノードは 2i+1, 2i+2 になる
            self._tree[i] = self._segfunc(self._tree[i * 2 + 1], self._tree[i * 2 + 2])

    def query(self, a: int, b: int) -> int:
        """
        区間 [a, b) で segfuncを実行した結果を返す
        計算量 O(logN)

        Args:
            a (int): 区間の最初のインデックス(区間に含む)
            b (int): 区間の最後のインデックス(区間に含まない)

        Returns:
            int: 区間 [a, b) の最小値
        """
        return self._sub_query(a, b, 0, 0, self._n)

    def _sub_query(self, a: int, b: int, k: int, l: int, r: int) -> int:
        """
        _summary_

        Args:
            a (int): _description_
            b (int): _description_
            k (int): 現在見ているself._treeの位置
            l (int): self._tree[k]が表している区間の開始位置(lを含む)
            r (int): self._tree[k]が表している区間の終了位置(rを含まない)

        Returns:
            int: _description_
        """
        if r <= a or b <= l:
            return self._init_val
        elif a <= l and r <= b:
            return self._tree[k]
        else:
            vl = self._sub_query(a, b, k * 2 + 1, l, (l + r) // 2)  # 左側子要素
            vr = self._sub_query(a, b, k * 2 + 2, (l + r) // 2, r)  # 右側子要素
            return self._segfunc(vl, vr)
