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


def main():
    N, K = map(int, input().split())
    S = input()

    nex = string_next(S)

    ans = ""
    k = 0
    for i in range(K):
        for ordc in range(26):
            j = nex[k][ordc]
            if j == -1:
                continue

            if N - j - 1 >= K - i - 1:
                ans += chr(ord("a") + ordc)
                k = j + 1
                break

    print(ans)


if __name__ == "__main__":
    main()
