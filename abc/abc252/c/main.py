import math


def main():
    N = int(input())
    S = [input() for _ in range(N)]

    D = {str(i): set() for i in range(10)}
    for s in S:
        for i, si in enumerate(s):
            while i in D[si]:
                i += 10

            D[si].add(i)

    ans = math.inf
    for v in D.values():
        ans = min(ans, max(v))
    print(ans)


if __name__ == "__main__":
    main()
