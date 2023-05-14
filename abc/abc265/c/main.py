from queue import Queue

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]

    h, w = 0, 0
    q = Queue()
    q.put((h, w))
    visited = set()
    while not q.empty():
        vh, vw = q.get()
        if (vh, vw) in visited:
            print(-1)
            exit()

        visited.add((vh, vw))
        s = G[vh][vw]
        
        if s == "U" and vh - 1 >= 0:
            q.put((vh - 1, vw))
        if s == "D" and vh + 1 <= H - 1:
            q.put((vh + 1, vw))
        if s == "L" and vw - 1 >= 0:
            q.put((vh, vw - 1))
        if s == "R" and vw + 1 <= W - 1:
            q.put((vh, vw + 1))

    print(vh + 1, vw + 1)


if __name__ == "__main__":
    main()