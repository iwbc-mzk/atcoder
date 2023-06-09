from collections import defaultdict


def main():
    N = int(input())

    S = defaultdict(int)
    for _ in range(N):
        s = input()
        if s in S:
            print(f"{s}({S[s]})")
        else:
            print(s)

        S[s] += 1


if __name__ == "__main__":
    main()
