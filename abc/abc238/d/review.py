def main():
    T = int(input())

    for _ in range(T):
        a, s = map(int, input().split())
        if s < 2 * a:
            print("No")
        else:
            r = s - 2 * a
            rr = reversed(bin(r)[2:])
            aa = reversed(bin(a)[2:])
            for ai, ri in zip(aa, rr):
                if ri == '1' and ai == ri:
                    print("No")
                    break
            else:
                print("Yes")


if __name__ == "__main__":
    main()
