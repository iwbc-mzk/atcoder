from collections import defaultdict


def main():
    H, W = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(H)]

    ans = 0
    for hs in range(1 << H):
        h_num = 0
        for k in range(H):
            if hs >> k & 1:
                h_num += 1

        if hs == 6:
            pass

        count = defaultdict(int)
        for w in range(W):
            c_val = -1
            ok = True
            for k in range(H):
                if not (hs & 1 << k):
                    continue

                if c_val == -1:
                    c_val = P[k][w]
                else:
                    if c_val != P[k][w]:
                        ok = False
                        break

            if ok and c_val != -1:
                count[c_val] += 1
        else:
            for key, val in count.items():
                ans = max(ans, val * h_num)

    print(ans)


if __name__ == "__main__":
    main()
