def main():
    K = int(input())

    s = set()
    surplus = 0
    i = 0
    while True:
        surplus = (surplus + 7 * pow(10, i, K)) % K
        if surplus in s:
            print(-1)
            return

        if surplus == 0:
            print(i + 1)
            return
        else:
            s.add(surplus)

        i += 1


if __name__ == "__main__":
    main()
