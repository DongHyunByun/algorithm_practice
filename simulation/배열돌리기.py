from copy import deepcopy
from itertools import permutations

N,M,K=map(int,input().split())
L=[]
rot=[]

for i in range(N):
    L.append(list(map(int,input().split())))

for i in range(K):
    rot.append(list(map(int,input().split())))

def value(L):
    candi=[]
    for i in L:
        candi.append(sum(i))
    return min(candi)

def rotate(myL,r,c,s):
    '''
    print("회전이전")
    for i in myL:
        print(i)
    '''

    dR=[0,1,0,-1]
    dC=[1,0,-1,0]
    r-=1
    c-=1
    #테두리 k마다
    for k in range(1,s+1):
        i=r-k
        j=c-k
        temp=myL[i][j]
        for line in range(4):
            num=0
            while(num!=2*k):
                i=i+dR[line]
                j=j+dC[line]
                myL[i][j],temp=temp,myL[i][j]
                num+=1
    '''
    print("회전확인")
    for i in myL:
        print(i)
    '''

ans=99999999999
perL=list(permutations([i for i in range(K)],K))

#경우의 수 시작
for pL in perL:
    nowL = deepcopy(L)
    for p in pL:
        r=rot[p][0]
        c=rot[p][1]
        s=rot[p][2]
        rotate(nowL,r,c,s)
    tempV=value(nowL)
    if tempV<ans:
        ans=tempV

print(ans)