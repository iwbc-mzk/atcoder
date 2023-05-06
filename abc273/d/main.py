def move(rs: int, cs: int, d: str, l: int, walls: set, H: int, W: int):
    pos_r, pos_c = rs, cs
    for _ in range(l):
        if d == "L" and (pos_r, pos_c - 1) not in walls and pos_c - 1 > 0:
            pos_c -= 1
            continue

        if d == "R" and (pos_r, pos_c + 1) not in walls and pos_c + 1 <= W:
            pos_c += 1
            continue

        if d == "U" and (pos_r - 1, pos_c) not in walls and pos_r - 1 > 0:
            pos_r -= 1
            continue

        if d == "D" and (pos_r + 1, pos_c) not in walls and pos_r + 1 <= H:
            pos_r += 1
            continue

        break

    return pos_r, pos_c

def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    walls = {tuple(map(int, input().split())) for _ in range(N)}
    
    Q = int(input())
    pos = (rs, cs)
    for _ in range(Q):
        d, l = input().split()
        l = int(l)

        pos = move(*pos, d, l, walls, H, W)
        print(*pos)

if __name__ == "__main__":
    main()