from collections import deque


def main():
    H, W = map(int, input().split())

    rs, cs = map(int, input().split())
    rs, cs = rs - 1, cs - 1

    rt, ct = map(int, input().split())
    rt, ct = rt - 1, ct - 1

    S = [input() for _ in range(H)]

    # D = [[[10**8 for _ in range(4)] for _ in range(W)] for _ in range(H)]
    D = [10**18 for _ in range(H * W * 4)]

    q = deque()
    for i in range(4):
        q.append((rs, cs, i))
        D[rs * W * 4 + cs * 4 + i] = 0

    DRC = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        r, c, dir = q.popleft()
        for i in range(4):
            # 来た方向に戻るのは考えない
            if abs(dir - i) == 2:
                continue

            dr, dc = DRC[i]
            rr, cc = r + dr, c + dc
            if 0 <= rr < H and 0 <= cc < W and S[rr][cc] == ".":
                cost = D[(r * W + c) * 4 + dir] + (0 if dir == i else 1)

                if cost < D[(rr * W + cc) * 4 + i]:
                    if dir == i:
                        q.appendleft((rr, cc, i))
                    else:
                        q.append((rr, cc, i))
                    D[(rr * W + cc) * 4 + i] = cost

    ans = 10**18
    for i in range(4):
        ans = min(ans, D[(rt * W + ct) * 4 + i])
    print(ans)


if __name__ == "__main__":
    main()
