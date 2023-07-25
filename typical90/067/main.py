def base10int(decima_value: int, base: int) -> int:
    if decima_value // base:
        return int(
            str(base10int(decima_value // base, base)) + str(decima_value % base)
        )
    return int(decima_value % base)


def convert(N):
    # 10進数変換
    N10 = int(str(N), 8)

    # 9進数変換
    N9 = base10int(N10, 9)

    N8 = int(str(N9).replace("8", "5"))
    return N8


def main():
    N, K = map(int, input().split())

    for _ in range(K):
        N = convert(N)

    print(N)


if __name__ == "__main__":
    main()
