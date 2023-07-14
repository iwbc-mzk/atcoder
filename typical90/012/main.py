from collections import deque


from collections import defaultdict
from typing import Hashable, List
import sys

sys.setrecursionlimit(10**8)


class UnionFind:
    def __init__(self) -> None:
        self._parents: dict = defaultdict(lambda: -1)
        self._size: dict = defaultdict(lambda: 1)

    def root(self, x: Hashable) -> Hashable:
        if self._parents[x] == -1:
            return x
        else:
            # 経路圧縮
            self._parents[x] = self.root(self._parents[x])
            return self._parents[x]

    def is_same(self, x: Hashable, y: Hashable) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: Hashable, y: Hashable) -> None:
        rx = self.root(x)
        ry = self.root(y)

        if rx == ry:
            return

        # Union By Size
        if self._size[rx] < self._size[ry]:
            rx, ry = ry, rx

        self._parents[ry] = rx
        self._size[rx] += self._size[ry]

    def size(self, x: Hashable) -> int:
        return self._size[self.root(x)]

    def members(self, x: Hashable) -> List[Hashable]:
        rx = self.root(x)
        return [i for i in self._parents.keys() if self.root(i) == rx]

    def roots(self):
        return [key for key, val in self._parents.items() if val == -1]

    def group_count(self):
        return len(self.roots())


def main():
    H, W = map(int, input().split())
    Q = int(input())

    G = UnionFind()
    R = set()
    for _ in range(Q):
        i, *args = map(int, input().split())
        if i == 1:
            r, c = args
            if (r, c) == (4, 4):
                pass
            R.add((r, c))

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 1 <= r + dr <= H and 1 <= c + dc <= W:
                    if (r + dr, c + dc) in R:
                        G.unite((r, c), (r + dr, c + dc))
        else:
            ra, ca, rb, cb = args
            # if (ra, ca, rb, cb) == (4, 2, 3, 5):
            #     pass
            if (ra, ca) not in R or (rb, cb) not in R:
                print("No")
                continue

            if (ra, ca) == (rb, cb) and (ra, ca) in R:
                print("Yes")
                continue

            if G.is_same((ra, ca), (rb, cb)):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
