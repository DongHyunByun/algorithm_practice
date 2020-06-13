from collections import deque
from copy import deepcopy
dR=[0,0,-1,1]
dC=[1,-1,0,0]
def toInt(myL):
    word=""
    for i in range(3):
        word+="".join(myL[i])
    return int(word)

L=[]
iniR=0
iniC=0
for i in range(3):
    temp=list(input().split())
    if "0" in temp:
        iniR=i
        iniC=temp.index("0")
    L.append(temp)

q=deque([[L,iniR,iniC,0]])
visitedS=set([toInt(L)])
ans=-1
while(q):
    nowL,r,c,cnt=q.popleft()
    '''
    print(cnt,"번째")
    for i in nowL:
        print(i)
    '''
    # 정답이면?
    word=toInt(nowL)
    if word==123456780:
        ans=cnt
        break

    #이동하기
    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<3 and 0<=tempC<3:
            nowL[r][c],nowL[tempR][tempC]=nowL[tempR][tempC],nowL[r][c]
            tempWord=toInt(nowL)
            if tempWord not in visitedS:
                visitedS.add(tempWord)
                q.append([deepcopy(nowL),tempR,tempC,cnt+1])
            nowL[r][c], nowL[tempR][tempC] = nowL[tempR][tempC], nowL[r][c]

print(ans)

