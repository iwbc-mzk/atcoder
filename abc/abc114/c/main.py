import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    ans = []

    def rec(i, v):
        if v > N:
            return

        str_v = str(v)
        for j in "357":
            if j not in str_v:
                break
        else:
            ans.append(v)

        for n in [3, 5, 7]:
            rec(i + 1, 10 * v + n)

    rec(0, 0)
    print(len(ans))


if __name__ == "__main__":
    main()
