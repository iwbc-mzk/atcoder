from collections import defaultdict
from typing import Hashable, List


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
    N, M = map(int, input().split())
    ABC = [tuple(map(int, input().split())) for _ in range(M)]
    ABC.sort(key=lambda x: x[2])

    uf = UnionFind()
    ans = 0
    for a, b, c in ABC:
        if c < 0:
            uf.unite(a, b)
        else:
            if uf.root(a) == uf.root(b):
                ans += c
                continue
            else:
                uf.unite(a, b)

    print(ans)


if __name__ == "__main__":
    main()
