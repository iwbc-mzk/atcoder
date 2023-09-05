import sys
from itertools import permutations

sys.setrecursionlimit(10**9)


def main():
    T = int(input())

    for _ in range(T):
        R, G, B = map(int, input().split())
        RGB = [R, G, B]

        ans = float("inf")
        for i, j, k in permutations(range(3), 3):
            a, b, c = RGB[i], RGB[j], RGB[k]
            if abs(a - b) % 3:
                continue

            if a > b:
                a, b = b, a

            # ans_t = a + (b - a) // 3 + 2 * (b - a) // 3
            ans_t = b

            ans = min(ans, ans_t)

        if ans != float("inf"):
            print(ans)
        else:
            print(-1)


if __name__ == "__main__":
    main()
