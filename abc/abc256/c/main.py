def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    ans = 0
    for i11 in range(1, 31):
        for i12 in range(1, 31):
            if i11 + i12 >= h1:
                break
            i13 = h1 - i11 - i12

            for i21 in range(1, 31):
                for i22 in range(1, 31):
                    if i21 + i22 >= h2:
                        break
                    i23 = h2 - i21 - i22

                    i31 = w1 - i11 - i21
                    i32 = w2 - i12 - i22
                    i33 = w3 - i13 - i23

                    if i31 + i32 + i33 == h3 and i31 > 0 and i32 > 0 and i33 > 0:
                        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
