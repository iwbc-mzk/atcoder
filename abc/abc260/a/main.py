from collections import defaultdict


def main():
    S = input()

    cnt = defaultdict(int)
    for s in S:
        cnt[s] += 1

    for k, c in cnt.items():
        if c == 1:
            print(k)
            return
    else:
        print(-1)


if __name__ == "__main__":
    main()
