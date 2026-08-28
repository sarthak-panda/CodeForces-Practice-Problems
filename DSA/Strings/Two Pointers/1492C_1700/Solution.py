def solve() -> None:
    n, m = map(int, input().split())
    s = input().strip()
    t = input().strip()

    left = [0] * m
    right = [0] * m

    j = 0
    for i in range(n):
        if s[i] == t[j]:
            left[j] = i
            j += 1
            if j == m:
                break

    j = m - 1
    for i in range(n - 1, -1, -1):
        if s[i] == t[j]:
            right[j] = i
            j -= 1
            if j < 0:
                break

    ans = 0
    for i in range(m - 1):
        ans = max(ans, right[i + 1] - left[i])

    print(ans)


if __name__ == "__main__":
    solve()
