
for t in range(int(input())):
    tri=0
    N,M = map(int,input().split())
    L=[[] for i in range(N-1)] 
    pair=[]
    for m in range(M):
        a,b= map(int,input().split())
        L[a-1].append(b)
    for n in range(N-2):
        for i in range(len(L[n])):
            for j in range(i+1,len(L[n])):
                a=L[n][i]
                b=L[n][j]
                if ( (a < b) and (b in L[a-1]) )  :
                    tri+=1
                elif ((a > b) and (a in L[b-1]) ) :
                    tri+=1
    print(f"#{t+1} {tri}")
               
