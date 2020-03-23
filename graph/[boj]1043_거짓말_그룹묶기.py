from collections import deque

N,M=map(int,input().split())
L=list(map(int,input().split()))
knowSize=L.pop(0)
party=[]
peopleSize=[]
for i in range(M):
    temp=list(map(int, input().split()))
    peopleSize.append(temp.pop(0))
    party.append(temp)


# 중복된사람들 있는 파티들끼리 연결
graph={}
for i in range(M):
    graph[i]=[]
for i in range(M):
    for j in range(i+1,M):
        # 두 파티에 중복된 사람이 있으면 연결
        if set(party[i])&set(party[j]):
            graph[i].append(j)
            graph[j].append(i)
#print(graph)

# 서치
ans=0
visited=[0 for i in range(M)]
for i in range(M):
    if visited[i]==0:
        #print(i,"번파티 탐색시작")
        cnt=1
        canLie=True
        q=deque([i])
        visited[i]=1
        if set(party[i])&set(L):
            canLie=False
        while(q):
            temp=q.popleft()
            for conNode in graph[temp]:
                if not visited[conNode]:
                    #진실아는자가 잇는지
                    if set(party[conNode])&set(L):
                        canLie=False
                    cnt+=1
                    visited[conNode]=1
                    q.append(conNode)
        if canLie:
            #print("이파티그룹은 가능, 파티개수는 : ",cnt)
            ans+=cnt

print(ans)
