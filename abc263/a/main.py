from collections import defaultdict

def main():
    A, B, C, D, E = map(int, input().split())

    d = defaultdict(int)
    for v in [A, B, C, D, E]:
        d[v] += 1

    if len(d) == 2:
        for v in d.values():
            if v not in [2, 3]:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
        
if __name__ == "__main__":
    main()