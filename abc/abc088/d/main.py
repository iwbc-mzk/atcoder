from queue import Queue

def main():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        # 白マス=1, 黒マス=0
        conv = lambda x: 1 if x == "." else 0
        S.append(list(map(conv, list(input()))))

    q = Queue()
    start = (0, 0)
    q.put(start)
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    dist[0][0] = 0
    while not q.empty():
        h, w = q.get()
        
        up = (h-1, w)
        down = (h+1, w)
        right = (h, w+1)
        left = (h, w-1)

        for v in [up, down, right, left]:
            vh, vw = v
            if 0 <= vh < H and 0 <= vw < W:
                if not S[vh][vw]:
                    continue
            
                if dist[vh][vw] != -1:
                    dist[vh][vw] = min(dist[h][w] + 1, dist[vh][vw])
                else:
                    dist[vh][vw] = dist[h][w] + 1
                    q.put(v)
    
    if dist[H-1][W-1] == -1:
        print(-1)
    else:
        white_sum = sum(sum(v) for v in S)
        print(white_sum - (dist[H-1][W-1] + 1))


if __name__ == "__main__":
    main()