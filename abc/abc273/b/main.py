from decimal import Decimal, ROUND_HALF_UP
def main():
    X, K = map(int, input().split())
    X = Decimal(X)
    for i in range(K):
        X = X.quantize(Decimal(f"1E{i + 1}"), rounding=ROUND_HALF_UP)

    print(int(X))

if __name__ == "__main__":
    main()