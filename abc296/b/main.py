def main():
    S = [list(input()) for _ in range(8)]

    for i, si in enumerate(reversed(S)):
        for j, sj in enumerate(si):
            if sj == "*":
                print(f"{chr(97+j)}{chr(49+i)}")
                break


if __name__ == "__main__":
    main()