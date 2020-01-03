def numOfAbled(L,k):
    hori=0
    verti=0
    for i in range(len(L)):
        for j in range(len(L)-k+1):
            num=0
            for m in range(k):
                if L[i][j+m]!=1:
                    break
                else :
                    num+=1
            if num==k:
                if j==len(L)-k:
                    if L[i][j-1]==0 :
                        verti+=1
                elif j==0:
                    if L[i][j+k]==0:
                        verti+=1
                elif L[i][j+k]==0 and L[i][j-1]==0:
                    verti+=1

    for j in range(len(L)):
        for i in range(len(L)-k+1):
            num=0
            for m in range(k):
                if L[i+m][j]!=1:
                    break
                else :
                    num+=1
            if num==k:
                if i==len(L)-k:
                    if L[i-1][j]==0:
                        hori+=1
                elif i==0 :
                    if L[i+k][j]==0:
                        hori+=1
                elif L[i-1][j]==0 and L[i+k][j]==0:
                    hori+=1

    return verti+hori





for t in range(int(input())):
    L=[]
    [N,K] =list(map(int,input().split()))
    for n in range(N):
        L.append(list(map(int,input().split())))
    print(f"#{t+1} {numOfAbled(L,K)}")
