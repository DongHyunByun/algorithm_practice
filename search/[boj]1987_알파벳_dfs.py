dR=[0,0,-1,1]
dC=[1,-1,0,0]

R,C=map(int,input().split())
L=[]
for i in range(R):
    L.append(list(input()))

ans=0
def dfs(i,j,word):
    #print(i,j,word)
    global ans
    for k in range(4):
        tempR=i+dR[k]
        tempC=j+dC[k]
        if 0<=tempR<R and 0<=tempC<C:
            size=len(word)
            #알파뱃 중복되면 종료
            if L[tempR][tempC] in word:
                if ans<size:
                    ans=size
                continue
            else:
                dfs(tempR,tempC,word+L[tempR][tempC])

dfs(0,0,L[0][0])
print(ans)

