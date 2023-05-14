def main():
    S = list(input())
    
    I = {s: i for i, s in enumerate("atcoder")}

    ans = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if I[S[i]] > I[S[j]]:
                ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()