import heapq
from collections import defaultdict
from typing import Iterable, TypeVar, Optional

T = TypeVar("T")


class Multiset:
    def __init__(self, init_val: Iterable[T] = []) -> None:
        self._add_list = list(init_val)
        heapq.heapify(self._add_list)
        self._add_inv_list = [-v for v in init_val]
        heapq.heapify(self._add_inv_list)

        self._add_cnt: dict[T, int] = defaultdict(int)
        for a in self._add_list:
            self._add_cnt[a] += 1

        self._del_list: list[T] = []
        self._del_inv_list: list[T] = []

    def __len__(self) -> int:
        return self.size()

    def __contains__(self, value: T) -> bool:
        return self.count(value) > 0

    def add(self, value: T) -> None:
        """
        要素追加
        計算量: O(log N)

        Args:
            value (T): _description_
        """
        heapq.heappush(self._add_list, value)
        heapq.heappush(self._add_inv_list, -value)
        self._add_cnt[value] += 1

    def remove(self, value: T) -> None:
        """
        要素削除
        計算量: O(log N)

        Args:
            value (T): _description_

        Raises:
            ValueError: _description_
        """
        if self._add_cnt[value] > 0:
            heapq.heappush(self._del_list, value)
            heapq.heappush(self._del_inv_list, -value)
            self._add_cnt[value] -= 1
        else:
            raise ValueError(f"[{value}] does not exist.")

    def smallest(self) -> Optional[T]:
        while self._del_list and self._add_list[0] == self._del_list[0]:
            heapq.heappop(self._add_list)
            heapq.heappop(self._del_list)

        return self._add_list[0] if self.size() else None

    def largest(self) -> Optional[T]:
        while self._del_inv_list and self._add_inv_list[0] == self._del_inv_list[0]:
            heapq.heappop(self._add_inv_list)
            heapq.heappop(self._del_inv_list)

        return -self._add_inv_list[0] if self.size() else None

    def size(self) -> int:
        return len(self._add_list) - len(self._del_list)

    def is_empty(self) -> bool:
        return self.size() == 0

    def count(self, value: T) -> int:
        return self._add_cnt[value]


def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = []
    am = A[:M]
    am.sort()
    v = sum(am[:K])
    lm, rm = Multiset(am[:K]), Multiset(am[K:])
    for i in range(N - M + 1):
        if i == 0:
            ans.append(v)
            continue

        al, ar = A[i - 1], A[i + M - 1]
        if al in lm:
            lm.remove(al)
            v -= al
        else:
            rm.remove(al)

        rm.add(ar)
        while len(lm) < K:
            s = rm.smallest()
            rm.remove(s)
            lm.add(s)
            v += s

        while lm and rm and lm.largest() > rm.smallest():
            ll = lm.largest()
            lm.remove(ll)
            v -= ll

            rs = rm.smallest()
            rm.remove(rs)

            lm.add(rs)
            v += rs
            rm.add(ll)

        ans.append(v)

    print(*ans)


if __name__ == "__main__":
    main()
