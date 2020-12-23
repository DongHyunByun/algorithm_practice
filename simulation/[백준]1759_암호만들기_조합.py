from itertools import combinations
mo=["a","e","i","o","u"]

def makePass(mT,jT):
    temp=[]
    for i in mT:
        temp.append(myMo[i])
    for i in jT:
        temp.append(myJa[i])
    temp.sort()

    return "".join(temp)

L,C=map(int,input().split())
word=input().split()
myMo=[]
myJa=[]
for alpha in word:
    if alpha in mo:
        myMo.append(alpha)
    else:
        myJa.append(alpha)
sizeMo=len(myMo)
sizeJa=len(myJa)

m=[0]
for i in range(1,L-1):
    m.append(list(combinations([j for j in range(sizeMo)], i)))

j=[0,0]
for i in range(2,L):
    j.append(list(combinations([j for j in range(sizeJa)],i)))


#모음의 개수
ans=[]
for i in range(1,L-1):
    mCase=m[i]
    jCase=j[L-i]

    for mTuple in mCase:
        for jTuple in jCase:
            ans.append(makePass(mTuple,jTuple))

ans.sort()
for i in ans:
    print(i)