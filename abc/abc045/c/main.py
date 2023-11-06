import sys

sys.setrecursionlimit(10**9)


def main():
    S = input()

    ans = 0
    for i in range(2 ** (len(S) - 1)):
        vals = []
        val = ""
        for j, s in enumerate(S):
            val += s
            if (i >> j) & 1:
                vals.append(int(val))
                val = ""
        else:
            if val:
                vals.append(int(val))
                val = ""

        ans += sum(vals)

    print(ans)


if __name__ == "__main__":
    main()
