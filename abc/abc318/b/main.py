import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    AB, CD = [], []
    for _ in range(N):
        A, B, C, D = map(int, input().split())
        AB.append((A, B))
        CD.append((C, D))

    ans = 0
    for x in range(101):
        for y in range(101):
            for (a, b), (c, d) in zip(AB, CD):
                if a <= x < b and c <= y < d:
                    ans += 1
                    break

    print(ans)


if __name__ == "__main__":
    main()
