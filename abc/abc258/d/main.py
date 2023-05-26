import math

def main():
    N, X = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]

    AB_sum = [0]
    for a, b in AB:
        AB_sum.append(AB_sum[-1] + a + b)
    
    ans = math.inf
    for i, (a, b) in enumerate(AB, 1):
        if i > X:
            break

        t = AB_sum[i] + b * (X - i)
        ans = min(ans, t)

    print(ans)


if __name__ == "__main__":
    main()
