from collections import defaultdict

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]

    result = defaultdict(int)
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                for k in range(1, max(H, W)):
                    if i - k < 0 or i + k > H - 1 or j - k < 0 or j + k > W - 1:
                        break

                    if C[i - k][j - k] == C[i + k][j - k] == C[i - k][j + k] ==  C[i + k][j + k] == "#":
                        continue
                    else:
                        break

                result[k - 1] += 1
    
    ans = []
    for r in range(1, min(H, W) + 1):
        ans.append(str(result[r]))

    print(" ".join(ans))


if __name__ == "__main__":
    main()