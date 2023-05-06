from collections import defaultdict
 
memo = defaultdict(lambda: defaultdict(lambda:None))
 
def rec(idx, coins, X, price):
    if idx >= len(coins):
        return False
    
    if memo[idx][price] is not None:
        return memo[idx][price]
    
    flg = False
    A, B = coins[idx]
    for i in range(B+1):
        next_price = price + A*i
        if next_price == X:
            return True
        elif next_price > X:
            continue
        
        flg |= rec(idx+1, coins, X, next_price)
 
    memo[idx][price] = flg
 
    return flg
 
def main():
    N, X = map(int, input().split())
 
    coins = []
    for _ in range(N):
        A, B = map(int, input().split())
        coins.append((A, B))
 
    result = rec(0, coins, X, 0)
    print("Yes" if result else "No")
 
 
if __name__ == "__main__":
    main()