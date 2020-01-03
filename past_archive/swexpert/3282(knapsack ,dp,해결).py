def knapsack(K,N,listOfThing):
    L=[[0 for col in range(K+1)] for row in range(N+1)]
    for i in range(N+1):
        for j in range(K+1):
            if i==0 or j==0:
                continue
            elif (j-listOfThing[i-1][0])>=0:
                L[i][j]=max(L[i-1][j],L[i-1][j-listOfThing[i-1][0]]+listOfThing[i-1][1])
            else:
                L[i][j]=L[i-1][j]
    return L[N][K]



for t in range(int(input())):
    #N: 물건의 개수, K:최대부피
    N,K=map(int,input().split())


    # [n][0]:부피, [n][1]:가치
    listOfThing=[]
    for i in range(N):
        listOfThing.append(list(map(int,input().split())))
    print(f"#{t+1} {knapsack(K,N,listOfThing)}")
