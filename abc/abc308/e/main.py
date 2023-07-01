from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = input()

    D = {"M": defaultdict(int), "E": defaultdict(int), "X": defaultdict(int)}
    for i, s in enumerate(S):
        D[s][(A[i])] += 1

    ans = 0

    # 1 (1なし かつ ０あり)
    c = (D["M"][0] + D["M"][2]) * (D["E"][0] + D["E"][2]) * (D["X"][0] + D["X"][2])
    c -= D["M"][2] * D["E"][2] * D["X"][2]
    ans += c

    # 2 (2なし, 0, 1あり)
    c = (D["M"][0] + D["M"][1]) * (D["E"][0] + D["E"][1]) * (D["X"][0] + D["X"][1])
    c -= D["M"][0] * D["E"][0] * D["X"][0] + D["M"][1] * D["E"][1] * D["X"][1]
    ans += c * 2

    # 3 (0, 1, 2あり)
    c = sum(D["M"].values()) * sum(D["E"].values()) * sum(D["X"].values())
    c -= (D["M"][0] + D["M"][1]) * (D["E"][0] + D["E"][1]) * (D["X"][0] + D["X"][1])
    c -= (D["M"][0] + D["M"][2]) * (D["E"][0] + D["E"][2]) * (D["X"][0] + D["X"][2])
    c -= (D["M"][1] + D["M"][2]) * (D["E"][1] + D["E"][2]) * (D["X"][1] + D["X"][2])
    c += (
        (D["M"][0] * D["E"][0] * D["X"][0])
        + (D["M"][1] * D["E"][1] * D["X"][1])
        + (D["M"][2] * D["E"][2] * D["X"][2])
    )
    ans += c * 3

    print(ans)


if __name__ == "__main__":
    main()
