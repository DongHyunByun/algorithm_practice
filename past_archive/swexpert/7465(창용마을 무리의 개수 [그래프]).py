from collections import deque

for t in range(int(input())):
    N,M=map(int,input().split())
    graph=[]
    for i in range(M):
        graph.append(list(map(int,input().split())))
    totalL=[i for i in range(1,N+1)]
    ans=0
    for i in graph:
        if len(i)==1:
            graph.remove(i)
            totalL.remove(i[0])
            ans+=1



    while totalL:
        i=totalL[0]
        myStack=deque([i])
        while myStack:
            num=myStack.pop()
            totalL.remove(num)
            for j in graph:
                if (num in j) :
                    temp=list(j)
                    temp.remove(num)
                    if (temp[0] in totalL) and (temp[0] not in myStack):
                        myStack.extend([temp[0]])
        ans+=1
    print(f"#{t+1} {ans}")
