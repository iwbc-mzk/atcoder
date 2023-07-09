def main():
    N, A, B = map(int, input().split())

    ans = []
    for nr in range(N):
        for a in range(A):
            l = []
            for nc in range(N):
                m = "#" if (nr + nc) % 2 else "."
                for b in range(B):
                    l.append(m)

            ans.append(l)

    for a in ans:
        print("".join(a))


if __name__ == "__main__":
    main()
