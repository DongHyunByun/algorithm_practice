
from collections import deque

# 새로 추가되는 pair가 포함되어 있는 graph가 사이클인지만 확인하면 된다.
def isCycle(L,pair):
    tempL=[]
    for i in L:
        tempL.append(list(i))

    myStack=deque([])
    visitedNode=[]
    for i in tempL:
        if pair[1] in i:
            myStack.extend([pair[1]])
            break

    while myStack:
        Node=myStack.pop()
        visitedNode.extend([Node])
        throwL=[]
        for i in tempL:
            if Node in i:
                if pair[2] in i:           
                    return True
                throwL.append(i)
                if i[1]==Node:
                    myStack.extend([i[2]])
                else:
                    myStack.extend([i[1]])
        for i in throwL:
            tempL.remove(i)

    return False
        


for t in range(int(input())):
    N=int(input())
    L=[]
    for i in range(2):
        L.append(list(map(int,input().split())))
    E=float(input())
    
    #graph는 [거리, 노드1, 노드2]
    graph=[]
    
    for i in range(N):
        for j in range(i+1,N):
            dis=(pow(L[0][i]-L[0][j],2)+pow(L[1][i]-L[1][j],2))**(1.0/2.0)
            graph.append([dis,i,j])

    graph.sort()    
    

    #kruscal 알고리즘
    kruscalL=[]
    ans=0

    for i in range(len(graph)):
        if not isCycle(kruscalL,graph[i]):
            kruscalL.append(graph[i])
            ans+=E*pow(graph[i][0],2)
 
        if len(kruscalL)==N-1:
            break
        
    print(f"#{t+1} {round(ans)}")
