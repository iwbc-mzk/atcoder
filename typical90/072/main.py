from collections import defaultdict


def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]

    G = defaultdict(set)
    for h in range(H):
        for w in range(W):
            if C[h][w] == "#":
                continue

            for dh, dw in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                hh, ww = h + dh, w + dw
                if 0 <= hh < H and 0 <= ww < W and C[hh][ww] == ".":
                    G[(h, w)].add((hh, ww))

    ans = -1
    for h in range(H):
        for w in range(W):
            if C[h][w] == "#":
                continue

            start = (h, w)
            visited = set()
            visited.add(start)

            def dfs(v, d):
                nonlocal ans
                for vv in G[v]:
                    if vv == start and d + 1 >= 4:
                        ans = max(ans, d + 1)
                        break

                    if vv not in visited:
                        visited.add(vv)
                        dfs(vv, d + 1)
                        visited.remove(vv)

                return -1

            dfs(start, 0)

    print(ans)


if __name__ == "__main__":
    main()
