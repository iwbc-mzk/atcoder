def main():
    N = int(input())

    ans = set()
    def rec(i, n):
        if i > len(bin(N)) - 2:
            return
        
        if N >> i & 1:
            ans.add(n + 2 ** i)
            rec(i + 1, n + 2 ** i)

        rec(i + 1, n)
        ans.add(n)

    rec(0, 0)
    for a in sorted(ans):
        print(a)



if __name__ == "__main__":
    main()