from collections import deque


for t in range(10):
    isP=False
    t,N=list(map(int,input().split()))
    node=[i for i in range(100)]
    temp=list(map(int,input().split()))
    graph=[]
    
    for i in range(N):
        graph.append([temp[2*i], temp[2*i+1]])
    stack=deque([0])
    node.remove(0)
    while stack:
        startNode=stack.pop()
        for i in graph:
            if (i[0]==startNode) and (i[1] in node) :
                if (i[1]==99):
                    isP=True
                    break
                else:
                    stack.append(i[1])
                    node.remove(i[1])
                    
        if isP:
            break
        
    
    if isP:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")


