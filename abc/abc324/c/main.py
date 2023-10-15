import sys

sys.setrecursionlimit(10**9)


def main():
    N, T = input().split()
    N = int(N)
    S = [input() for _ in range(N)]

    ans = []
    for i, Si in enumerate(S, 1):
        if abs(len(T) - len(Si)) > 1:
            continue

        jt, js = 0, 0
        err = 0
        while jt < len(T) and js < len(Si):
            if T[jt] == Si[js]:
                jt += 1
                js += 1
            else:
                err += 1
                if err <= 1:
                    if len(Si) < len(T):
                        jt += 1
                    elif len(Si) > len(T):
                        js += 1
                    else:
                        jt += 1
                        js += 1
                else:
                    break
        else:
            ans.append(i)

    ans.sort()
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
