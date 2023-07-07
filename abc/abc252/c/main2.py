import math


def main():
    N = int(input())
    S = [input() for _ in range(N)]

    ans = math.inf
    for l in range(10):
        l = str(l)
        t = 0
        stopped = set()
        while len(stopped) < N:
            for i, s in enumerate(S):
                if s[t % 10] == l and i not in stopped:
                    stopped.add(i)
                    break
            t += 1

        ans = min(ans, t - 1)

    print(ans)


if __name__ == "__main__":
    main()
