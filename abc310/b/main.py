def main():
    N, M = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            Pi, Ci, *Fi = P[i]
            Pj, Cj, *Fj = P[j]

            if Pi >= Pj:
                func_flg = Ci <= Cj
                for fi in Fi:
                    if fi not in Fj:
                        func_flg = False
                        break

                if not func_flg:
                    continue

                if Pi > Pj or Ci < Cj:
                    print("Yes")
                    return
    else:
        print("No")


if __name__ == "__main__":
    main()
