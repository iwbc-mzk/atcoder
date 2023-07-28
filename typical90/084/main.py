from typing import Iterable


# ランレングス圧縮
def run_length_encoding(s: Iterable):
    pre = s[0]
    cnt = 0
    result = []
    for si in s:
        if si == pre:
            cnt += 1
        else:
            result.append((pre, cnt))
            pre = si
            cnt = 1
    else:
        result.append((pre, cnt))

    return result


def main():
    N = int(input())
    S = input()

    s = run_length_encoding(S)
    ans = (N + 1) * (N) // 2
    for _, c in s:
        ans -= (c + 1) * c // 2

    print(ans)
    pass


if __name__ == "__main__":
    main()
