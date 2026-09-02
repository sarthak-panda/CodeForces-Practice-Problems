import sys
from collections import deque

def solve():
    global n,adj
    #define root
    root=0
    ans,dp,num_nodes_in_subtree_inc_root=[0]*n,[0]*n,[0]*n
    #bfs
    q,order,par=deque([root]),[],[-1]*n
    while q:
        c=q.popleft()
        order.append(c)
        for v in adj[c]:
            if(v!=par[c]):
                par[v]=c
                q.append(v)
    #dp depends on child, so let us visit in reverse order
    for nd in reversed(order):
        num_nodes_in_subtree_inc_root[nd],dp[nd]=1,0
        for v in adj[nd]:
            if v!=par[nd]:
                num_nodes_in_subtree_inc_root[nd]+=num_nodes_in_subtree_inc_root[v]
                dp[nd]+=(dp[v]+num_nodes_in_subtree_inc_root[v])
    #compute ans
    ans[root]=dp[root]
    #re-root's recursion needs to be computed for parent's first
    for nd in order:
        if par[nd]!=-1:#nd!=root
            ans[nd]=ans[par[nd]]+n-2*num_nodes_in_subtree_inc_root[nd]
    return ans

input = sys.stdin.readline
n=int(input())
adj=[[] for _ in range(n)]
for _ in range(n-1):
    u,v=map(int,input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

print(*solve())