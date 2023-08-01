from collections import defaultdict, deque
from typing import List, TypeVar, Iterable

_T = TypeVar("_T")


class SCC:
    """
    強連結成分分解
    """

    def __init__(self, vertexes: Iterable[_T]) -> None:
        self._vertexes = set(vertexes)

        self._G = defaultdict(set)
        self._rev_G = defaultdict(set)

        self._components: List[_T] = []

    def add_ege(self, from_, to) -> None:
        if from_ not in self._vertexes or to not in self._vertexes:
            raise ValueError()

        self._G[from_].add(to)
        self._rev_G[to].add(from_)

        if self._components:
            self._components = []

    def _orders(self) -> List[_T]:
        """
        DFSの帰りがけ順で頂点に番号を振る
        """
        orders = []
        visited = set()
        for s in self._vertexes:
            if s in visited:
                continue

            q = deque()
            q.append(s)
            while q:
                v = q.pop()
                if v < 0:
                    orders.append(-v)
                    continue

                if v in visited:
                    continue

                visited.add(v)
                q.append(-v)

                for vv in self._G[v]:
                    if vv in visited:
                        continue
                    q.append(vv)

        orders.reverse()

        return orders

    def _divide_components(self):
        components = []

        visited = set()
        for i in self._orders():
            if i in visited:
                continue

            q = deque()
            q.append(i)
            visited.add(i)
            u = set()
            while q:
                v = q.pop()
                u.add(v)

                for vv in self._rev_G[v]:
                    if vv not in visited:
                        q.append(vv)
                        visited.add(vv)

            components.append(u)

        return components

    def components(self) -> None:
        if self._components:
            return self._components

        self._components = self._divide_components()

        return self._components


def main():
    N, M = map(int, input().split())

    scc = SCC(range(1, N + 1))
    for _ in range(M):
        A, B = map(int, input().split())
        scc.add_ege(A, B)

    ans = 0
    for comp in scc.components():
        ans += len(comp) * (len(comp) - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
