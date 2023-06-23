from collections import deque

MOD = 998244353


def main():
    Q = int(input())

    S = 1
    num = deque()
    num.append(S)
    for _ in range(Q):
        q, *x = map(int, input().split())
        if q == 1:
            x = x[0]
            S *= 10
            S %= MOD
            S += x % MOD
            S %= MOD
            num.append(x)
        elif q == 2:
            t = num.popleft()

            tmp = t % MOD
            tmp *= pow(10, len(num), MOD)
            tmp %= MOD

            S -= tmp
            S %= MOD
        else:
            print(S)


if __name__ == "__main__":
    main()
