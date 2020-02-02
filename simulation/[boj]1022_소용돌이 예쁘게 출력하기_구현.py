r1,c1,r2,c2=map(int,input().split())
toNum=max(map(abs,[r1,c1,r2,c2]))

def isIn(i,j):
    if 0<=i<r2-r1+1 and 0<=j<c2-c1+1:
        return True
    return False

L=[[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

dR=[-1,0,1,0,0]
dC=[0,-1,0,1,1]

if isIn(-r1,-c1):
    L[-r1][-c1]=1
r=-r1
c=-c1+1
num=2

lastNum=0
for cell in range(1,toNum+1):
    for k in range(4):
        for move in range(cell*2):
            if isIn(r,c):
                L[r][c] = num
                lastNum=num
            num += 1
            if move==cell*2-1 :
                k+=1
            r=r+dR[k]
            c=c+dC[k]

numlen=0
while(lastNum!=0):
    lastNum=lastNum//10
    numlen+=1

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print("%*d"%(numlen,L[i][j]),end=" ")
    print()