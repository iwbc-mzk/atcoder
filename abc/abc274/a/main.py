from decimal import Decimal, ROUND_HALF_UP

def main():
    A, B = map(int, input().split())
    print(Decimal(B / A).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))


if __name__ == "__main__":
    main()