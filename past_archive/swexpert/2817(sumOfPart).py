def timesOfCase(sum,index):
    if index==N:
        if sum==K:
            return 1
        else:
            return 0
    pick=timesOfCase(sum+L[index],index+1)
    unpick=timesOfCase(sum,index+1)
    return pick+unpick


for t in range(int(input())):
    L=[]
    N,K=map(int,input().split())
    L.extend(list(map(int,input().split())))
    print(f"#{t+1} {timesOfCase(0,0)}")
