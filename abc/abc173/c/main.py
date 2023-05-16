from itertools import combinations
from collections import defaultdict

def main():
    H, W, K = map(int, input().split())
    C = [list(input()) for _ in range(H)]

    total = 0
    counts_row = defaultdict(int)
    for i, c in enumerate(C):
        cnt = c.count("#")
        counts_row[i] += cnt
        total += cnt

    counts_col = defaultdict(int)
    for col_i in range(W):
        for row_i in range(H):
            if C[row_i][col_i] == "#":
                counts_col[col_i] += 1

    comb_row = [[-1]]
    for i in range(1, H + 1):
        comb_row += list(combinations(range(H), i))
    
    comb_col = [[-1]]
    for i in range(1, W + 1):
        comb_col += list(combinations(range(W), i))

    ans = 0
    for c_row in comb_row:
        for c_col in comb_col:

            removed = 0
            for i, row in enumerate(c_row):
                if row >= 0:
                    removed += counts_row[row]
                for col in c_col:
                    if i == 0 and col >= 0:
                        removed += counts_col[col]
                    if row >= 0 and col >= 0 and C[row][col] == "#":
                        removed -= 1
            if total - removed == K:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()