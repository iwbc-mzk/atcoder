def main():
    N = int(input())
    P = list(map(int, input().split()))

    cnt = [0 for _ in range(N)]
    for i, p in enumerate(P):
        for j in range(3):
            cnt[(p - 1 - i + j + N) % N] += 1
        
    ans = 0
    for c in cnt:   
        ans = max(ans, c)
    
    print(ans)

if __name__ == "__main__":
    main()