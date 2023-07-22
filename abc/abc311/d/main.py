from collections import deque


def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]

    visited = set([(1, 1)])
    started = set([(1, 1)])
    q = deque()
    q.append((1, 1))
    while q:
        x, y = q.pop()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if S[ny][nx] == ".":
                i = 1
                while True:
                    nx, ny = x + i * dx, y + i * dy
                    if S[ny][nx] == ".":
                        i += 1
                        visited.add((nx, ny))
                    else:
                        break

                nx, ny = nx - dx, ny - dy
                if (nx, ny) not in started:
                    q.append((nx, ny))
                    started.add((nx, ny))

    print(len(visited))


if __name__ == "__main__":
    main()
