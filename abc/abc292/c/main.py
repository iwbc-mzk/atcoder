import math


def main():
    N = int(input())

    ans = 0
    for x in range(1, N):
        ab = x
        cd = N - x

        ab_cnt = 0
        a = 1
        while a <= math.sqrt(ab):
            if ab % a == 0:
                ab_cnt += 1
                if a != ab / a:
                    ab_cnt += 1
            a += 1

        cd_cnt = 0
        c = 1
        while c <= math.sqrt(cd):
            if cd % c == 0:
                cd_cnt += 1
                if c != cd / c:
                    cd_cnt += 1
            c += 1

        ans += ab_cnt * cd_cnt

    print(ans)


if __name__ == "__main__":
    main()
