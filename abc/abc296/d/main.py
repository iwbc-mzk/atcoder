import math

def main():
    N, M = map(int, input().split())

    
    ans = -1
    for a in range(1, N+1):
        b = math.ceil(M / a)
        if b <= N:
            if ans == -1:
                ans = a * b
            else:
                ans = min(ans, a * b)

            if a > b:
                break

    print(ans)


if __name__ == "__main__":
    main()