def solve(s,t,n,m):
    L,R=[0]*m,[0]*m
    
    j=0
    for i in range(n):
        if(s[i]==t[j]):
            L[j]=i
            j+=1
            if(j==m):
                break
    
    j=m-1
    for i in range(n-1,-1,-1):
        if(s[i]==t[j]):
            R[j]=i
            j-=1
            if(j==-1):
                break
    
    return max(R[i+1]-L[i] for i in range(m-1))

n,m=map(int,input().split())
s=input()
t=input()
print(solve(s,t,n,m))