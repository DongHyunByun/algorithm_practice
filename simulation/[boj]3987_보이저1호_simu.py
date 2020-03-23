N,M=map(int,input().split())
dR=[-1,0,1,0]
dC=[0,1,0,-1]
direction=["U","R","D","L"]
rightUp=[1,0,3,2]
leftUp=[3,2,1,0]

L=[]
for i in range(N):
    L.append(list(input()))
PR,PC=map(int,input().split())
PR-=1
PC-=1
ansL=[]

#네방향시작
for k in range(4):
    r=PR
    c=PC
    to=k
    time=0
    isInf=False
    while(1):
        #이동
        r+=dR[to]
        c+=dC[to]
        #시간경과
        time+=1
        #경우확인
        if 0<=r<N and 0<=c<M:
            if L[r][c]=="/":
                to=rightUp[to]
            elif L[r][c]=="\\":
                to=leftUp[to]
            elif L[r][c]=="C":
                ansL.append(time)
                break
        else:
            ansL.append(time)
            break

        if r==PR and c==PC and to==k:
            infTo=k
            isInf=True
            break

    if isInf:
        break

if isInf:
    print(direction[infTo])
    print("Voyager")
else:
    #print(ansL)
    maxNum=max(ansL)
    print(direction[ansL.index(maxNum)])
    print(maxNum)

