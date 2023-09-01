import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = list(input())

    D = [[] for _ in range(26)]
    for i, s in enumerate(S):
        D[ord(s) - ord("a")].append(i)

    i = 0
    r = N + 1
    while i < N and i < r:
        for a in range(26):
            if (ord(S[i]) - ord("a")) <= a:
                break

            while D[a]:
                rr = D[a].pop()
                if i < rr < r:
                    S[i], S[rr] = S[rr], S[i]
                    r = rr
                    break
            else:
                continue

            break
        i += 1

    print("".join(S))


if __name__ == "__main__":
    main()
