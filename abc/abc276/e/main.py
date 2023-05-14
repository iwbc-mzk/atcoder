from queue import Queue

def main():
    H, W = map(int, input().split())

    C = []
    for i in range(1, H + 1):
        c = input()
        start_idx = c.find("S")
        if start_idx >= 0:
            start = (i, start_idx + 1)
        C.append(list(c))

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    firsts = set()
    for i, j in move:
        h, w = start[0] + i, start[1] + j
        if 0 < h <= H and 0 < w <= W and C[h - 1][w - 1] == ".":
            firsts.add((h, w))

    for first in firsts:
        q = Queue()
        q.put(first)
        visited = set()
        visited.add(start)
        visited.add(first)
        while not q.empty():
            h, w = q.get()
            for x, y in move:
                vh, vw = h + x, w + y
                if 0 < vh <= H and 0 < vw <= W:
                    if C[vh - 1][vw - 1] == "." and (vh, vw) not in visited:
                        if (vh, vw) != first and (vh, vw) in firsts:
                            print("Yes")
                            exit()
                        visited.add((vh, vw))
                        q.put((vh, vw))
    print("No")




if __name__ == "__main__":
    main()