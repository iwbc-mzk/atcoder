import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

import heapq
from collections import defaultdict
from typing import Iterable, TypeVar, Optional

T = TypeVar("T")


class Multiset:
    def __init__(self, init_val: Iterable[T] = []) -> None:
        self._add_list = list(init_val)
        heapq.heapify(self._add_list)

        self._add_cnt: dict[T, int] = defaultdict(int)
        for a in self._add_list:
            self._add_cnt[a] += 1

        self._del_list: list[T] = []

    def __len__(self) -> int:
        return self.size()

    def __contains__(self, value: T) -> bool:
        return self.count(value) > 0

    def add(self, value: T) -> None:
        heapq.heappush(self._add_list, value)
        self._add_cnt[value] += 1

    def discard(self, value: T) -> None:
        if self._add_cnt[value] > 0:
            heapq.heappush(self._del_list, value)
            self._add_cnt[value] -= 1
        else:
            raise ValueError(f"[{value}] does not exist.")

    def smallest(self) -> Optional[T]:
        while self._del_list and self._add_list[0] == self._del_list[0]:
            heapq.heappop(self._add_list)
            heapq.heappop(self._del_list)

        return self._add_list[0] if self.size() else None

    def size(self) -> int:
        return len(self._add_list) - len(self._del_list)

    def is_empty(self) -> bool:
        return self.size() == 0

    def count(self, value: T) -> int:
        return self._add_cnt[value]


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    ms = Multiset()
    for i in range(N + 1):
        ms.add(i)

    C = defaultdict(int)
    for a in A:
        C[a] += 1
        if C[a] > 0 and a in ms:
            ms.discard(a)

    for _ in range(Q):
        i, x = map(int, input().split())
        a = A[i - 1]
        A[i - 1] = x
        C[a] -= 1
        C[x] += 1

        if x in ms:
            ms.discard(x)

        if C[a] == 0:
            ms.add(a)

        print(ms.smallest())


if __name__ == "__main__":
    main()
