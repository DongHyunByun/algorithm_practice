def score (m,f,repo):
    return m*0.35+f*0.45+repo*0.2

def alpa (total,rank):
    import math
    n=math.ceil(rank/(total/10))
    if n==1:
        return "A+"
    elif n==2:
        return "A0"
    elif n==3:
        return "A-"
    elif n==4:
        return "B+"
    elif n==5:
        return "B0"
    elif n==6:
        return "B-"
    elif n==7:
        return "C+"
    elif n==8:
        return "C0"
    elif n==9:
        return "C-"
    else:
        return "D0"

for t in range(int(input())):
    N,K=input().split()
    L=[]
   
    for i in range(int(N)):
        a=list(map(int,input().split()))
        L.append([score(a[0],a[1],a[2]),i+1])
    L.sort(reverse=True)
    for j in range(len(L)):
        if L[j][1]==int(K):
            print(f"#{t+1} {alpa(int(N),j+1)}")