def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S_sorted = sorted(S)
    
    result = {}
    for i, s in enumerate(S_sorted):
        left = i - 1 if i - 1 >= 0 else 0
        right = i + 2 if i - 2 <= N else N
        d = S_sorted[left:right]
        l = -1
        while len(d) > 1:
            l += 1
            if l >= len(s):
                l = len(s)
                break

            t = []
            for di in d:
                if l < len(di) and s[l] == di[l]:
                    t.append(di)
            d = t
        result[s] = l
    
    for s in S:
        print(result[s])

if __name__ == "__main__":
    main()