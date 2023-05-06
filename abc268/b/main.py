def main():
    S = input()
    T = input()

    ans = "Yes" if T.startswith(S) else "No"
    print(ans)


if __name__ == "__main__":
    main()