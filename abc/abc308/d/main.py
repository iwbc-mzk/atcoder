from collections import deque


def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    SNUKE = "snuke"

    if S[0][0] != SNUKE[0]:
        print("No")
        return

    q = deque()
    q.append((0, 0, 0))
    visited = set()
    visited.add((0, 0))
    while q:
        i, j, n = q.pop()

        s = SNUKE[(n + 1) % len(SNUKE)]
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ii = i + di
            jj = j + dj
            if not (0 <= ii < H) or not (0 <= jj < W):
                continue

            if S[ii][jj] == s and (ii, jj) not in visited:
                if (ii, jj) == (H - 1, W - 1):
                    print("Yes")
                    return

                q.append((ii, jj, n + 1))
                visited.add((ii, jj))

    print("No")


if __name__ == "__main__":
    main()
