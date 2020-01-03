#겹치는경우 제외

for t in range(int(input())):
    N,X=map(int,input().split())
    L=[]
    ans=0
    for i in range(N):
        L.append(list(map(int,input().split())))

    LforC=[]
    for i in range(len(L[0])):
        LforC.append([temp[i] for temp in L])
    sumL=L+LforC
    
    for i in sumL:
        taken=[0 for _ in range(len(i))]
        nowNum=i[0]
        isPos=True
        for j in range(1,len(i)):
            if nowNum>i[j]:
                if nowNum-i[j]!=1:
                    isPos=False
                    break
                if (j<=len(i)-X):
                    for k in range(X):
                        taken[j+k]+=1
                        if i[j+k]!=i[j] or taken[j+k]>=2:
                            isPos=False
                            break
                else:
                    isPos=False
                    break
            elif nowNum<i[j]:
                if i[j]-nowNum!=1:
                    isPos=False
                    break
                if (j>=X):
                    for k in range(X):
                        taken[j-k-1]+=1
                        if i[j-k-1]!=i[j-1] or taken[j-k-1]>=2:
                            isPos=False
                            break
                else:
                    isPos=False
                    break
            nowNum=i[j]
        if isPos:
            print(i)
            ans+=1
        
    print(f"#{t+1} {ans}")