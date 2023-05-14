from collections import defaultdict

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    
    dp = [[[-1 for _ in range(D)] for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
        
    for n in range(N):
        for k in range(K+1):
            for d in range(D):
                if dp[n][k][d] == -1:
                    continue

                # a_nを選ばない場合
                dp[n+1][k][d] = max(dp[n+1][k][d], dp[n][k][d])

                # a_nを選ぶ場合
                if k < K:
                    dp[n+1][k+1][(d+A[n])%D] = max(dp[n+1][k+1][(d+A[n])%D], dp[n][k][d] + A[n])
    
    print(dp[N][K][0])


if __name__ == "__main__":
    main()
