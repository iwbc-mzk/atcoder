from collections import defaultdict


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    D = defaultdict(set)
    for i, a in enumerate(A, 1):
        D[a].add(i)

    t = len(D[0])  # 0になったかごの数
    d = list(D.items())
    d.sort()
    prev = 0  # 食べきったかごのリンゴ数の初期値
    k = K  # 食べなくてはいけないリンゴの数
    for cnt, s in d:
        if cnt == 0:
            continue
        else:
            v = (N - t) * (cnt - prev)  # cnt個入ったかごが0になる時の食べたリンゴの数
            if v <= k:
                k -= v
                prev = cnt
                t += len(s)
            else:
                break

    ans = []
    # 残りk個はからになっていないかごで等分
    kk = k // (N - t) if N - t > 0 else 0
    # 余りは最初のかごから順番に消費する
    r = k % (N - t) if N - t > 0 else 0
    for a in A:
        a = max(0, a - prev)
        if k > 0 and a > 0:
            a -= kk
            k -= kk
            if r > 0:
                a -= 1
                k -= 1
                r -= 1
        ans.append(a)

    print(*ans)


if __name__ == "__main__":
    main()
