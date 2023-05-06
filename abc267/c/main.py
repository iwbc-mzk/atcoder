def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    ans = 0
    prev_sum = 0
    for n in range(N):
        if n + M - 1 > N - 1:
            break
        
        if n == 0:
            a = A[n:n + M]
            prev_sum = sum(a)
            for i, ai in enumerate(a, 1):
                ans += i * ai
            prev_ans = ans
        else:
            prev_ans = prev_ans - prev_sum + A[n + M - 1] * M
            ans = max(ans, prev_ans)
            prev_sum = prev_sum - A[n - 1] + A[n + M - 1]
    
    print(ans)
        


if __name__ == "__main__":
    main()