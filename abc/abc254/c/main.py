from collections import defaultdict


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    AA = defaultdict(list)
    for i, a in enumerate(A):
        AA[i % K].append(a)

    for k in AA:
        AA[k].sort(reverse=True)

    s = []
    for i in range(N):
        s.append(AA[i % K].pop())

    for i in range(N - 1):
        if s[i] > s[i + 1]:
            print("No")
            return
    else:
        print("Yes")


if __name__ == "__main__":
    main()
