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
