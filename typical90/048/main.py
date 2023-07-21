def main():
    N, K = map(int, input().split())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append(B)
        AB.append(A - B)

    AB.sort(reverse=True)

    ans = 0
    for k in range(K):
        ans += AB[k]

    print(ans)


if __name__ == "__main__":
    main()
