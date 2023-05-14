from collections import defaultdict

def main():
    H, W, N, h, w = map(int, input().split())
    A = [input().split() for _ in range(H)]

    d = defaultdict(lambda: [W, 0, H, 0][:]) # list = [x_min, x_max, y_min, y_max]
    for i in range(H):
        for j in range(W):
            v = A[i][j]
            d[v][0] = min(d[v][0], j) # x_min
            d[v][1] = max(d[v][1], j) # x_max
            d[v][2] = min(d[v][2], i) # y_min
            d[v][3] = max(d[v][3], i) # y_max

    k_max = H - h
    l_max = W - w
    ans = [[-1 for _ in range(l_max+1)] for _ in range(k_max+1)]
    for k in range(k_max+1):
        for l in range(l_max+1):
            cnt = 0
            for v, (x_min, x_max, y_min, y_max) in d.items():
                if k <= y_min and y_max <= k+h-1:
                    if l <= x_min and x_max <= l+w-1:
                        continue
                cnt += 1
            ans[k][l] = str(cnt)
                

    for a in ans:
        print(" ".join(a))


if __name__ == "__main__":
    main()