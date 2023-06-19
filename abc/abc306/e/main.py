import heapq
from collections import defaultdict
from typing import Iterable, TypeVar, List

T = TypeVar("T")


class Multiset:
    def __init__(self, init_val: Iterable[T] = []) -> None:
        self._add_list = list(init_val)
        heapq.heapify(self._add_list)

        self._add_cnt = defaultdict(int)
        for a in self._add_list:
            self._add_cnt[a] += 1

        self._del_list: List[T] = []

    def add(self, value: T) -> None:
        heapq.heappush(self._add_list, value)
        self._add_cnt[value] += 1

    def discard(self, value: T) -> None:
        if self._add_cnt[value] > 0:
            heapq.heappush(self._del_list, value)
            self._add_cnt[value] -= 1
        else:
            raise ValueError(f"[{value}] does not exist.")

    def smallest(self) -> T:
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
    N, K, Q = map(int, input().split())

    A1, A2 = Multiset(), Multiset()

    ans = 0
    num = [0 for _ in range(N)]
    for _ in range(Q):
        x, y = map(int, input().split())

        pre = num[x - 1]
        if pre and A1.count(pre):
            A1.discard(pre)
            ans -= pre
        elif pre and A2.count(-pre):
            A2.discard(-pre)
        num[x - 1] = y

        A2.add(-y)
        while A1.size() < K and not A2.is_empty():
            s = A2.smallest()
            A2.discard(s)
            A1.add(-s)
            ans += -s

        while (
            not A1.is_empty() and not A2.is_empty() and (A1.smallest() < -A2.smallest())
        ):
            s1 = A1.smallest()
            A1.discard(s1)
            s2 = -A2.smallest()
            A2.discard(-s2)

            A1.add(s2)
            A2.add(-s1)

            ans += s2 - s1

        print(ans)


if __name__ == "__main__":
    main()
