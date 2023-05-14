from collections import defaultdict

def main():
    S = list(input())
    T = list(input())

    t_len = len(T)
    r_cache = defaultdict(lambda: True)
    l_cache = defaultdict(lambda: True)
    s_prime = None
    for x in range(t_len + 1):
        l = t_len - x
        if not s_prime:
            s_prime = S[:x] + (S[-l:] if l > 0 else "")
        else:
            s_prime[x - 1] = S[x - 1]
        
        ans = True
        if x == 0:
            for i in reversed(range(t_len)):
                if s_prime[i] == T[i] or s_prime[i] == "?" or T[i] == "?":
                    r_cache[i] &= r_cache[i + 1]
                else:
                    r_cache[i] = False
            ans = r_cache[x]
        else:
            l_cache[x] = l_cache[x - 1] & (s_prime[x - 1] == T[x - 1] or s_prime[x - 1] == "?" or T[x - 1] == "?")
            ans = l_cache[x] & r_cache[x]

        print("Yes" if ans else "No")


if __name__ == "__main__":
    main()