from typing import List, Union, TypeVar

T = TypeVar("T")
Num = Union[int, float]


# 参考: https://algo-logic.info/segment-tree/
class LazySegTree:
    def __init__(self, init_list: List[Num], type_: str = "min") -> None:
        self._n = 1 << (len(init_list) - 1).bit_length()

        if type_ == "min":
            self._init_val = float("inf")
            self._segfunc_tt = lambda x1, x2: min(x1, x2)
            self._segfunc_tl = lambda x, m: x if m == self._init_val else m
            self._segfunc_ll = lambda m1, m2: min(m1, m2)
        elif type_ == "max":
            self._init_val = -float("inf")
            self._segfunc_tt = lambda x, y: max(x, y)
            self._segfunc_tl = lambda x, m: x if m == self._init_val else m
            self._segfunc_ll = lambda m1, m2: max(m1, m2)
        elif type_ == "sum":
            self._init_val = 0
            self._segfunc_tt = lambda x1, x2: x1 + x2
            self._segfunc_tl = lambda x, m: x + m
            self._segfunc_ll = lambda m1, m2: m1 + m2
        elif type_ == "product":
            self._init_val = 1
            self._segfunc_tt = lambda x1, x2: x1 * x2
            self._segfunc_tl = lambda x, m: x * m
            self._segfunc_ll = lambda m1, m2: m1 * m2
        else:
            raise ValueError()

        self._tree = [self._init_val] * 2 * self._n
        self._lazy = [self._init_val] * 2 * self._n

        for i, v in enumerate(init_list):
            self._tree[i + self._n - 1] = v
        for i in range(self._n - 2, -1, -1):
            self._tree[i] = self._segfunc_ll(
                self._tree[2 * i + 1], self._tree[2 * i + 2]
            )

    def _eval(self, k: int) -> None:
        if self._lazy[k] == self._init_val:
            return

        if k < self._n - 1:
            self._lazy[k * 2 + 1] = self._segfunc_ll(
                self._lazy[k * 2 + 1], self._lazy[k]
            )
            self._lazy[k * 2 + 2] = self._segfunc_ll(
                self._lazy[k * 2 + 2], self._lazy[k]
            )

        self._tree[k] = self._segfunc_tl(self._tree[k], self._lazy[k])
        self._lazy[k] = self._init_val

    def update(self, a: int, b: int, x: int) -> None:
        self._update(a, b, x, 0, 0, self._n)

    def _update(self, a: int, b: int, x: int, k: int, l: int, r: int) -> None:
        self._eval(k)
        if a <= l and r <= b:  # 完全に内側の時
            self._lazy[k] = self._segfunc_tt(self._lazy[k], x)
            self._eval(k)
        elif a < r and l < b:  # 一部区間が被る時
            self._update(a, b, x, k * 2 + 1, l, (l + r) // 2)  # 左の子
            self._update(a, b, x, k * 2 + 2, (l + r) // 2, r)  # 右の子
            self._tree[k] = self._segfunc_tt(
                self._tree[k * 2 + 1], self._tree[k * 2 + 2]
            )

    def query(self, a: int, b: int) -> int:
        return self._query(a, b, 0, 0, self._n)

    def _query(self, a: int, b: int, k: int, l: int, r: int) -> int:
        self._eval(k)
        if r <= a or b <= l:
            return self._init_val
        elif a <= l and r <= b:
            return self._tree[k]
        else:
            vl = self._query(a, b, k * 2 + 1, l, (l + r) // 2)  # 左側子要素
            vr = self._query(a, b, k * 2 + 2, (l + r) // 2, r)  # 右側子要素
            return self._segfunc_tt(vl, vr)


def main():
    W, N = map(int, input().split())

    st = LazySegTree([0 for _ in range(2 * N)], type_="max")

    # 座標圧縮
    LR = []
    for _ in range(N):
        L, R = map(int, input().split())
        LR.append(L)
        LR.append(R)
    lr = sorted(set(LR))
    D = {v: i for i, v in enumerate(lr)}

    for i in range(0, 2 * N, 2):
        L, R = LR[i], LR[i + 1]
        L, R = D[L], D[R]
        h = st.query(L, R + 1) + 1
        st.update(L, R + 1, h)

        print(h)


if __name__ == "__main__":
    main()
