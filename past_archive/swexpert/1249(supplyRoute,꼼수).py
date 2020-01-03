def find(L,LL,N):
    r=0
    c=0
    count=0
    myStack=[[r,c,count]]
    while myStack:
        u=myStack.pop()
        if (u[0]<0 or u[1]<0 or u[0]==N or u[1]==N):
            continue
        
        
        u[2]+=int(L[u[0]][u[1]])
        if (LL[u[0]][u[1]] >u[2]):
            LL[u[0]][u[1]]=u[2]
        else:
            continue

        if (LL[u[0]][u[1]]>LL[N-1][N-1]):
            continue

        myStack.extend( [[u[0]+1,u[1],u[2]],[u[0],u[1]-1,u[2]],[u[0]-1,u[1],u[2]],[u[0],u[1]+1,u[2]]] )

    
    return LL[N-1][N-1]
    
   
for t in range(int(input())):
    N=int(input())
    L=[]
    for i in range(N):
        temp=[]
        temp.extend(input())
        L.append(list(temp))

    #LL초기화 꼼수(90000으론 안돌아감)
    LL=[[1000 for i in range(N)] for j in range(N)]
    ans=find(L,LL,N)
    print(f"#{t+1} {ans}")
