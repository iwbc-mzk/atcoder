from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))

    c = Counter(A)
    cnt = 0
    for i, v in c.items():
        cnt += v//2

    print(cnt)

if __name__ == "__main__":
    main()