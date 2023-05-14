from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = defaultdict(int)
    ans[1] = 0
    for i, a in enumerate(A):
        ans[2 * (i + 1)] = ans[a] + 1
        ans[2 * (i + 1) + 1] = ans[a] + 1
    
    for i in range(1, 2 * N + 2):
        print(ans[i])



if __name__ == "__main__":
    main()