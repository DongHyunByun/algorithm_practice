import sys
U,N=map(int,input().split())
L=[]
priceCnt=[[] for i in range(U+1)] #해당인덱스 가격을 부른사람의 명단
for i in range(N):
    a,b=sys.stdin.readline().rstrip().split()
    priceCnt[int(b)].append(a)

#print(priceCnt)
minSize=100001
ans=""
price=0
for indx in range(U+1):
    tempSize=len(priceCnt[indx])
    if tempSize!=0 and tempSize<minSize :
        minSize=tempSize
        name=priceCnt[indx][0]
        price=indx

print(name,price)