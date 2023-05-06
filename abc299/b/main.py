def main():
    N, T = map(int, input().split())
    C = list(map(int, input().split()))
    R = list(map(int, input().split()))

    a_ans = 0
    a_max = 0
    b_ans = 0
    b_max = 0
    a = C[0]
    b = T
    for i, (c, r) in enumerate(zip(C, R), 1):
        if c == a:
            if r > a_max:
                a_ans = i
                a_max = r
        if c == b:
            if r > b_max:
                b_ans = i
                b_max = r
    
    if b_ans:
        print(b_ans)
    else:
        print(a_ans)


if __name__ == "__main__":
    main()