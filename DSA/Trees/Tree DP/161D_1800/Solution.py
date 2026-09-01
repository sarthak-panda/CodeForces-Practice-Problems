import sys

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
        
    dp1 = [[0] * (k + 1) for _ in range(n)]
    dp2 = [[0] * (k + 1) for _ in range(n)]
    
    # 1. BFS to get the top-down traversal order and parent mapping
    order = []
    q = [0]
    parent = [-1] * n
    
    for u in q:
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                q.append(v)
                
    # 2. Simulate dfs1 (Bottom-Up) by iterating in reverse ie child's first
    for u in reversed(order):
        dp1[u][0] = 1
        for v in adj[u]:
            if v != parent[u]:
                for d in range(1, k + 1):
                    dp1[u][d] += dp1[v][d - 1]
                    
    # 3. Simulate dfs2 (Top-Down) by iterating forward ie parent's first
    for u in order:
        p = parent[u]
        if p == -1:
            # Overwrite instead of .copy() to save memory/time
            for d in range(k + 1):
                dp2[u][d] = dp1[u][d]
        else:
            dp2[u][0] = 1
            if k >= 1:
                dp2[u][1] = dp1[u][1] + dp2[p][0]
            for d in range(2, k + 1):
                dp2[u][d] = dp1[u][d] + dp2[p][d - 1] - dp1[u][d - 2]
                
    # 4. Calculate total pairs
    res = 0
    for i in range(n):
        res += dp2[i][k]
        
    print(res // 2)

if __name__ == '__main__':
    solve()