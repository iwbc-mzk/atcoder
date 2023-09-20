def main():
    N = int(input())
    S = list(input())

    l, r_list = None, []
    t = 0
    for i, s in enumerate(S):
        if s == "p" and l is None:
            l = i

        if s == "p":
            t += 1
        else:
            if t:
                r_list.append(i - 1)
            t = 0
    else:
        if S[-1] == "p":
            r_list.append(N - 1)

    if l is not None and r_list:
        ans = []
        for ri in r_list:
            SS = S[:l] + list(reversed(S[l : ri + 1])) + S[ri + 1 :]
            t = []
            for i, s in enumerate(SS):
                if l <= i <= ri:
                    s = "p" if s == "d" else "d"
                t.append(s)

            ans.append("".join(t))
        ans.sort()

        print(ans[0])
    else:
        print("".join(S))


if __name__ == "__main__":
    main()
