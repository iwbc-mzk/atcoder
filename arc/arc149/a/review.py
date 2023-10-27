def main():
    N, M = map(int, input().split())

    nums = [0 for _ in range(9)]
    l = []
    for n in range(1, N + 1):
        for i in range(1, 10):
            num = nums[i - 1]
            num *= 10
            num += i
            num %= M
            nums[i - 1] = num
            if num == 0:
                l.append((n, i))

    if l:
        l.sort(reverse=True)
        ans = str(l[0][1]) * l[0][0]
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
