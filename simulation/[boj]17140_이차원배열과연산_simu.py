from copy import deepcopy
r,c,k=map(int,input().split())
r-=1
c-=1
L=[]
for i in range(3):
    L.append(list(map(int,input().split())))

nowR=3
nowC=len(L[0])

ans=0
while(1):
    '''
    print("변환전")
    for i in range(nowR):
        print(L[i])
    '''
    if ans == 101:
        print(-1)
        break
    try:
        if L[r][c]==k:
            print(ans)
            break
    except:
        pass
    #행연산
    if nowR>=nowC:
        newL=[]
        size = 0
        for i in range(nowR):
            dic = {}
            rL=[]
            for j in range(nowC):
                if L[i][j] in dic:
                    dic[L[i][j]]+=1
                else:
                    dic[L[i][j]]=1

            for key in dic:
                if key!=0:
                    rL.append([dic[key],key])
            temp=[]
            for case in sorted(rL):
                temp.extend([case[1],case[0]])
            tempSize=len(temp)
            if tempSize>size:
                size=tempSize
            newL.append(temp)
        for i in range(nowR):
            for j in range(size-len(newL[i])):
                newL[i].extend([0])
        nowC=size
        L=newL
    #열연산
    else:
        newL=[]
        size=0
        for j in range(nowC):
            dic = {}
            cL=[]
            for i in range(nowR):
                if L[i][j] in dic:
                    dic[L[i][j]]+=1
                else:
                    dic[L[i][j]]=1

            for key in dic:
                if key!=0:
                    cL.append([dic[key],key])
            temp=[]
            for case in sorted(cL):
                temp.extend([case[1],case[0]])
            tempSize=len(temp)
            if tempSize>size:
                size=tempSize
            newL.append(temp)
        for j in range(nowC):
            for i in range(size-len(newL[j])):
                newL[j].extend([0])
        nowR=size
        L=[[0 for j in range(nowC)] for i in range(nowR)]
        for j in range(nowC):
            for i in range(nowR):
                L[i][j]=newL[j][i]
    '''
    print("변환후")
    for i in range(nowR):
        print(L[i])
    '''
    ans+=1