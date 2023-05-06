def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]

    ans = []
    for j in range(W):
        s = 0
        for ch in C:
            if ch[j] == "#":
                s += 1
        ans.append(s)

    print(*ans)


if __name__ == "__main__":
    main()