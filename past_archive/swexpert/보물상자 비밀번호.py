def hexToTen(a):
    a.lower()
    return int(a,16)

for t in range(int(input())):
    N,K=map(int,input().split())
    L=list(input())
    ansL=[]
    #a개씩 4번 돌려 a개씩 끊기
    a=len(L)//4
    for i in range(a):
        for n in range(4):
            strNum="".join(L[a*n:a*(n+1)])
            ansL.append(strNum)
        L.insert(0,L.pop())

    
    ansL=list(set(ansL))
    ansL.sort(key=hexToTen,reverse=True)

    print(f"#{t+1} {hexToTen(ansL[K-1])}")