def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
 
    even = []
    odd = []
    ans = -1
    for a in reversed(A):
        if a % 2:
            odd.append(a)
        else:
            even.append(a)
 
        if len(even) == 2:
            ans = max(ans, sum(even))
        if len(odd) == 2:
            ans = max(ans, sum(odd))
        
        if len(even) >= 2 and len(odd) >= 2:
            break
    
    print(ans)
 
if __name__ == "__main__":
    main()