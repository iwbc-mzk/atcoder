def main():
    S = input()
    ans = S.rfind("a")
    print(ans+1 if ans >= 0 else ans)


if __name__ == "__main__":
    main()