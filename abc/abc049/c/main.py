def rec(i:int, S:str, options:list):
    if i == 0:
        return ""
    
    for j in range(len(options)):
        t = rec(i-1, S, options) + options[j]
        if t == S[:len(t)]:
            return True
        
    return False


def main():
    S = input()

    options = ["dream", "dreamer", "erase", "eraser"]
    N = len(S)
    dp = [False] * (N+1)
    dp[0] = True
    for i in range(N+1):
        for opt in options:
            l = len(opt)
            if i >= l and dp[i-l] and S[i-l:i] == opt:
                dp[i] = True

    print("YES" if dp[N] else "NO")

if __name__ == "__main__":
    main()