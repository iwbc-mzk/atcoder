from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 8)

def main():
    N, M = map(int, input().split())
    
    gragh = defaultdict(set)
    for _ in range(M):
        x, y = map(int, input().split())
        gragh[x].add(y)

    flg = [False for _ in range(N + 1)]
    dp = [0 for _ in range(N + 1)]
    def rec(x):
        if flg[x]:
            return dp[x]
        
        m = 0
        for v in gragh[x]:
            m = max(m, rec(v) + 1)

        dp[x] = m
        flg[x] = True
        return m

    ans = 0
    for n in range(1, N + 1):
        ans = max(ans, rec(n))    

    print(ans)
        

    


if __name__ == "__main__":
    main()