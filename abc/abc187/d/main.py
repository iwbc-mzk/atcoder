def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    B = []
    # 合計人数が大きい + 青木派が多い 順で降順ソート
    sorted_AB = sorted(AB, key=lambda x: sum(x) + x[0], reverse=True)

    a_total = sum([x[0] for x in sorted_AB])

    total = 0
    for i, (a, b) in enumerate(sorted_AB, 1):
        total += a + b
        a_total -= a
        if total > a_total:
            print(i)
            break


if __name__ == "__main__":
    main()
