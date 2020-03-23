from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]
L=[]
for i in range(5):
    L.append(input().split())
ansS=set([])

def dfs(r,c,word):
    if len(word)==6:
        ansS.add(word)
        return

    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<5 and 0<=tempC<5 :
            dfs(tempR,tempC,word+L[tempR][tempC])

for i in range(5):
    for j in range(5):
        dfs(i,j,L[i][j])
print(len(ansS))

