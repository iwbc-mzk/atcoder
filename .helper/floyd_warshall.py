from math import inf
from typing import TypeVar, List, Union, Dict

T = TypeVar("T")


def floyd_warshall(
    vertexes: List[T], weights: Dict[T, Dict[T, Union[int, float]]]
) -> Dict[T, Dict[T : Union[int, float]]]:
    """
    フロイド・ワーシャル法を用いて全頂点間の最短距離を求める。

    Args:
        vertexes (List[T]): 全頂点のリスト
        weights (Dict[T, Dict[T, Union[int, float]]]): 各辺の重み。無向グラフの場合は a->b, b->a 両方の重みが必要。

    Returns:
        Dict[T, Dict[T : Union[int, float]]]: 各頂点間の最短距離。infの場合は到達不可能を表す。
    """
    # 距離の初期化
    dist = {vartex1: {vartex2: inf for vartex2 in vertexes} for vartex1 in vertexes}
    for k in vertexes:
        dist[k][k] = 0
    for k1, d in weights.items():
        for k2, w in d.items():
            dist[k1][k2] = w

    for k in vertexes:
        for i in vertexes:
            for j in vertexes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
