def main():
    N = int(input())

    ans = ""
    nums = "0123456789ABCDEF"
    for i in reversed(range(2)):
        v = N // 16 ** i
        N %= 16 ** i
        ans += nums[v]

    print(ans)


if __name__ == "__main__":
    main()