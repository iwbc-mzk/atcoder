import sys

sys.setrecursionlimit(10**9)


def main():
    S = input()

    ans = 1
    for l in range(len(S)):
        for r in range(l, len(S)):
            ll, rr = l, r
            while ll < rr:
                if S[ll] != S[rr]:
                    break
                ll += 1
                rr -= 1
            else:
                ans = max(ans, r - l + 1)

    print(ans)


if __name__ == "__main__":
    main()
