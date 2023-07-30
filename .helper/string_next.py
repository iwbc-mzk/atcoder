from typing import List


def string_next(S: str) -> List[List[int]]:
    """
    nex[i][c] := i文字目以降で最初に文字cが登場するindex
    存在しない場合は -1
    """
    N = len(S)
    nex = [[-1 for _ in range(26)] for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(26):
            nex[i][j] = nex[i + 1][j]
        nex[i][ord(S[i]) - ord("a")] = i

    return nex
