import sys


def solve():
    input = sys.stdin.readline
    n = int(input())

    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)

    parent = [-1] * n
    depth = [0] * n
    order = [0]

    for u in order:
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            order.append(v)

    subtree_size = [1] * n
    root_sum = 0
    for u in range(n):
        root_sum += depth[u]

    for u in reversed(order):
        p = parent[u]
        if p != -1:
            subtree_size[p] += subtree_size[u]

    ans = [0] * n
    ans[0] = root_sum

    for u in order:
        for v in adj[u]:
            if v == parent[u]:
                continue
            ans[v] = ans[u] - subtree_size[v] + (n - subtree_size[v])

    print(*ans)


if __name__ == '__main__':
    solve()
