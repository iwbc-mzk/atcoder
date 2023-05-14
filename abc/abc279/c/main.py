from collections import Counter

def main():
    H, W = map(int, input().split())

    CS = [[] for _ in range(W)]
    for _ in range(H):
        for i, s in enumerate(input()):
            CS[i].append(s)
    
    CT = [[] for _ in range(W)]
    for _ in range(H):
        for i, s in enumerate(input()):
            CT[i].append(s)
    
    cnt_s = Counter(["".join(l) for l in CS])
    cnt_t = Counter(["".join(l) for l in CT])

    if cnt_s == cnt_t:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()