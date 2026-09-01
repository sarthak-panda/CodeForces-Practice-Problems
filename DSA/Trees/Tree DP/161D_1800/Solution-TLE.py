import sys
def dfs1(i,par):
    global k,adj,dp1 # else u can pass as argument
    for c in adj[i]:
        if c!=par: dfs1(c,i) # call for all children c
    # since dp1 is ready for children, compute for current for all distances
    dp1[i][0]=1
    for d in range(1,k+1):
        dp1[i][d]=0
        for c in adj[i]:
            if(c==par): continue #skip parent
            dp1[i][d]+=dp1[c][d-1]
def dfs2(i,par):
    global k,adj,dp1,dp2
    # we need to calculate for parent (ie current) before calling it's child in dfs
    # compute for all dist
    if(par==-1):#i.e. declared root
        dp2[i]=dp1[i].copy()
    else:
        dp2[i][0]=1#dp1[i][0]
        if k>=1: dp2[i][1]=dp1[i][1]+dp2[par][0]
        for d in range(2,k+1):
            dp2[i][d]=dp1[i][d]+dp2[par][d-1]-dp1[i][d-2]
    for c in adj[i]:
        if c!=par: dfs2(c,i)
def solve():
    global dp2
    root=0
    dfs1(root,-1)
    dfs2(root,-1)
    res=0
    for i in range(n):
        res+=dp2[i][k]
    return res//2
input = sys.stdin.readline
n,k=map(int, input().split())
adj=[[] for _ in range(n)]
dp1=[[0]*(k+1) for _ in range(n)]
dp2=[[0]*(k+1) for _ in range(n)]
for _ in range(n-1):
    u,v=map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)
print(solve())