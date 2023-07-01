from decimal import Decimal


def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    suc = []
    for i, (a, b) in enumerate(AB, 1):
        s = Decimal(str(a)) / Decimal(str(a + b))
        suc.append((s, i))

    suc.sort(key=lambda x: (x[0], -i), reverse=True)
    ans = []
    for a in suc:
        ans.append(a[1])

    print(*ans)


if __name__ == "__main__":
    main()
