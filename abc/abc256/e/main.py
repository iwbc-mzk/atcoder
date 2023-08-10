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
    N = int(input())
    X = list(map(int, input().split()))
    C = list(map(int, input().split()))

    uf = UnionFind()
    for i, x in enumerate(X, 1):
        uf.unite(i, x)

    ans = 0
    roots = uf.roots()
    for root in roots:
        size = uf.size(root)
        s = root
        for _ in range(size):
            s = X[s - 1]

        m = float("inf")
        visited = set()
        while s not in visited:
            visited.add(s)
            m = min(m, C[s - 1])
            s = X[s - 1]

        ans += m
    print(ans)


if __name__ == "__main__":
    main()
