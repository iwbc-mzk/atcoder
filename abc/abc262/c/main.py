def main():
    N = int(input())
    A = list(map(int, input().split()))

    m = [a == i for i, a in enumerate(A, 1)]
    match_cnt = sum(m)
    
    ans = 0
    for i, a in enumerate(A, 1):
        if a == i:
            ans += match_cnt - 1
        else:
            if A[a - 1] == i:
                ans += 1

    ans //= 2
    print(ans)


if __name__ == "__main__":
    main()