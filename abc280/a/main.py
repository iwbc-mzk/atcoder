def main():
    H, W = map(int, input().split())
    cnt = 0
    for _ in range(H):
        s = list(input())
        cnt += s.count("#")

    print(cnt)


if __name__ == "__main__":
    main()