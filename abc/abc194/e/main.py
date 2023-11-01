import sys

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
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    ms = Multiset()
    for i in range(N + 2):
        ms.add(i)

    C = [0 for _ in range(N)]
    ans = float("inf")
    for i, a in enumerate(A):
        if C[a] == 0:
            ms.discard(a)
        C[a] += 1

        if i < M - 1:
            continue
        elif i == M - 1:
            ans = min(ans, ms.smallest())
        else:
            C[A[i - M]] -= 1
            if C[A[i - M]] == 0:
                ms.add(A[i - M])
            ans = min(ans, ms.smallest())

    print(ans)


if __name__ == "__main__":
    main()
