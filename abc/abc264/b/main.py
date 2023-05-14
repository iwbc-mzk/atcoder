def main():
    R, C = map(int, input().split())
    dr, dc = abs(R - 8), abs(C -8)
    print("black" if max(dr, dc) % 2 else "white")


if __name__ == "__main__":
    main()