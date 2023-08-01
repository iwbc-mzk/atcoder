from typing import TypeVar
from collections import defaultdict
from math import inf
import heapq

T = TypeVar("T")


def dijkstra(
    gragh: dict[T, set], weights: dict[T, dict[T, int]], start: T, use_heap: bool = True
) -> dict[T, int]:
    """
    ダイクストラ法を用いて始点からの最短距離を求める

    Args:
        gragh (dict[T, set]): グラフ。全頂点の情報が必要。次数が0の頂点等の情報も必要。
        weights (dict[T, dict[T, int]]): 辺のコスト。
        start (T): 始点
        use_heap (bool, optional): 未処理中の最小距離をもつ頂点を取り出すのにheapを利用するか。
                                   疎グラフ(E=O(V))ならばFalseにしたほうが計算量は少ない。
                                   Defaults to True.

    Returns:
        dict[T, int]: _description_
    """
    visited = set()
    distances = defaultdict(lambda: inf)
    distances[start] = 0

    if use_heap:
        q = [(0, start)]
        while q:
            # 未処理の中で最小の距離を持つ頂点を取り出す
            dist, v = heapq.heappop(q)
            if v in visited:
                continue

            visited.add(v)

            for vv in gragh[v]:
                if vv in visited:
                    continue

                new_dist = dist + weights[v][vv]
                if new_dist < distances[vv]:
                    distances[vv] = new_dist
                    heapq.heappush(q, (new_dist, vv))
    else:
        # 確定済でない頂点のうち、dist値が最小の頂点を探す
        for _ in gragh:
            min_dist = inf
            min_v = -1
            for v in gragh:
                if v not in visited and distances[v] < min_dist:
                    min_dist = distances[v]
                    min_v = v

            # 見つからなければ終了する
            if min_v == -1:
                break

            # min_vを始点とした各辺を緩和する
            for v in gragh[min_v]:
                d = distances[min_v] + weights[min_v][v]
                distances[v] = min(distances[v], d)

            # min_vを確定済にする
            visited.add(min_v)

    return distances
