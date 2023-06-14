# ランレングス圧縮
def runLengthEncoding(s: str):
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
    S = input()
    T = input()

    s_enc = runLengthEncoding(S)
    t_enc = runLengthEncoding(T)

    if len(s_enc) != len(t_enc):
        print("No")
        return

    for (s_char, s_cnt), (t_char, t_cnt) in zip(s_enc, t_enc):
        if s_char != t_char:
            print("No")
            return
        else:
            if s_cnt == t_cnt or 2 <= s_cnt < t_cnt:
                continue
            else:
                print("No")
                return
    else:
        print("Yes")


if __name__ == "__main__":
    main()
