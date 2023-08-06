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
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    D = []
    for s in S:
        d = defaultdict(int)
        for si in s:
            d[si] += 1

        D.append(d)

    ans = 0
    for i in range(2**N + 1):
        ms = Multiset()
        for j in range(N):
            if i >> j & 1:
                for s in S[j]:
                    ms.add(s)

        a = 0
        for k in range(26):
            alp = chr(ord("a") + k)
            if ms.count(alp) == K:
                a += 1

        ans = max(ans, a)

    print(ans)


if __name__ == "__main__":
    main()
