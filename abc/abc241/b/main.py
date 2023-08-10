from collections import defaultdict


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = defaultdict(int)
    for a in A:
        C[a] += 1

    for b in B:
        if b not in C or C[b] == 0:
            print("No")
            return
        else:
            C[b] -= 1

    print("Yes")


if __name__ == "__main__":
    main()
