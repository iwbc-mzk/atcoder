from collections import defaultdict

def main():
    S = input()
    T = input()

    s_cnt = defaultdict(int)
    for s in S:
        s_cnt[s] += 1

    t_cnt = defaultdict(int)
    for t in T:
        t_cnt[t] += 1

    s_at = s_cnt["@"]
    t_at = t_cnt["@"]
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in "atcoder":
            if s_cnt[i] != t_cnt[i]:
                print("No")
                return

        if s_cnt[i] == t_cnt[i]:
            continue
        elif s_cnt[i] < t_cnt[i]:
            s_at -= t_cnt[i] - s_cnt[i]
        else:
            t_at -= s_cnt[i] - t_cnt[i]

    if s_at >= 0 and t_at >= 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()