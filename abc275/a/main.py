def main():
    N = int(input())
    H = list(map(int, input().split()))

    m = -1
    for i, h in enumerate(H):
        if h > m:
            m = h
            idx = i
    
    print(idx+1)

if __name__ == "__main__":
    main()