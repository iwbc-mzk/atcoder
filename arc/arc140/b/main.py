import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = input()

    odd = []
    even = []
    t = ""
    for i, s in enumerate(S):
        if len(t) < 3:
            t += s
        else:
            t = t[1:] + s

        if t == "ARC":
            l, r = i - 3, i + 1
            c = 0
            while 0 <= l and r <= N - 1:
                if S[l] == "A" and S[r] == "C":
                    c += 1
                else:
                    break
                l -= 1
                r += 1

            if c:
                odd.append(c)
            else:
                even.append(c)

    i = 1
    ans = 0
    while odd or even:
        if i % 2:
            if odd:
                odd[-1] -= 1
                if odd[-1] == 0:
                    even.append(odd.pop())
            else:
                i += 1
                continue
        else:
            if even:
                even.pop()
            else:
                odd.pop()

        ans += 1
        i += 1

    print(ans)


if __name__ == "__main__":
    main()
