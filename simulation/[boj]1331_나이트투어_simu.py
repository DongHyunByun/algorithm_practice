ans="Valid"
visited=[[0 for j in range(6)] for i in range(6)]

loc=input()
preR=ord(loc[0])-ord("A")
preC=int(loc[1])-1
startR=preR
startC=preC
visited[preR][preC]=1
for i in range(35):
    loc=input()
    r=ord(loc[0])-ord("A")
    c=int(loc[1])-1
    #이동가능확인
    if not (abs(preR-r)+abs(preC-c)==3 and preR!=r and preC!=c):
        #print(loc)
        ans="Invalid"
    #방문되었는지 확인
    if visited[r][c]==1:
        #print(loc)
        ans="Invalid"
    #마지막이면 처음자리로 왔는지 확인
    if i==34:
        if not (abs(r-startR)+abs(c-startC)==3 and r!=startR and c!=startC):
            #print(loc)
            ans="Invalid"
    visited[r][c]=1
    preR = r
    preC = c

print(ans)


