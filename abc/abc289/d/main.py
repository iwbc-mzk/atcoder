from collections import defaultdict

def main():
    N = int(input())
    A = set(map(int, input().split()))
    M = int(input())
    B = set(map(int, input().split()))
    X = int(input())

    dp = defaultdict(bool)
    dp[0] = True
    for x in range(1, X + 1):
        if x in B:
            continue

        for a in A:
            if x >= a:
                dp[x] |= dp[x - a]

    print("Yes" if dp[X] else "No")


if __name__ == "__main__":
    main()