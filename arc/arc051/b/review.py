# https://zenn.dev/wapa5pow/articles/arc051-b-a9ee813fd49725e802a7
def main():
    K = int(input())

    c = 0

    def rec(a, b):
        nonlocal c
        if c > K:
            return (a, b)
        else:
            c += 1
        return rec(a + b, a)

    ans = rec(1, 0)
    print(*ans)


if __name__ == "__main__":
    main()
