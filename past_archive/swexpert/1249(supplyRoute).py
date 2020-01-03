def find(r,c,n,count):
    global minSize

    #outrange이면 종료
    if (r<0 or c<0 or r==n or c==n):
        return 10000

    #도착지점이면 종료
    if (r==n-1 and c==n-1):
        if (count<minSize):
            minSize=count
        return 0
    
    count+=int(L[r][c])

    #현재까지 시간이 최소시간 이상이면 종료
    if count>minSize:
        return 10000
    
    return min(find(r+1,c,n,count),find(r,c+1,n,count),
               find(r-1,c,n,count),find(r,c-1,n,count))+int(L[r][c])
    
   
for t in range(int(input())):
    N=int(input())
    L=[]
    for i in range(N):
        temp=[]
        temp.extend(input())
        L.append(list(temp))

    minSize=100000
    LL=[[-1 for i in range(N)] for j in range(N)]
    ans=find(0,0,N,0)

    print(f"#{t+1} {ans}")


 '''
 #경로저장은 왜 안되는가?

 def find(r,c,n,count):
    global minSize

    #outrange이면 종료
    if (r<0 or c<0 or r==n or c==n):
        return 10000

    #도착지점이면 종료
    if (r==n-1 and c==n-1):
        if (count<minSize):
            minSize=count
        return 0
    
    count+=int(L[r][c])

    #현재까지 시간이 최소시간 이상이면 종료
    if count>minSize:
        return 10000
    
    if (LL[r][c]==-1):
        LL[r][c]=min(find(r+1,c,n,count),find(r,c+1,n,count),
                     find(r-1,c,n,count),find(r,c-1,n,count))+int(L[r][c])
        return LL[r][c]
    else:
        return LL[r][c]
    
   
for t in range(int(input())):
    N=int(input())
    L=[]
    for i in range(N):
        temp=[]
        temp.extend(input())
        L.append(list(temp))

    minSize=100000
    LL=[[-1 for i in range(N)] for j in range(N)]
    ans=find(0,0,N,0)
    print(LL)
    print(f"#{t+1} {ans}")
'''