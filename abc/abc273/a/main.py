def rec(n: int):
    if n == 0:
        return 1
    return n * rec(n - 1)

def main():
    N = int(input())
    print(rec(N))


if __name__ == "__main__":
    main()