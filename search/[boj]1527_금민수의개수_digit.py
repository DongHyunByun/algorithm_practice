from itertools import combinations
A,B=map(int,input().split())

goldNum=[]
for size in range(1,10):
    L=[i for i in range(size)]
    for numOfFour in range(size+1):
        indexOfFour=list(combinations(L,numOfFour))
        for case in indexOfFour:
            word = ["7" for i in range(size)]
            for i in case:
                word[i]="4"
            goldNum.append(int("".join(word)))

goldNum.sort()
sizeOfGoldNum=len(goldNum)

s=-1
for i in range(sizeOfGoldNum):
    if goldNum[i]>=A:
        s=i
        break
e=-1
for i in range(sizeOfGoldNum-1,-1,-1):
    if goldNum[i]<=B:
        e=i
        break
        
if s!=-1 and e!=-1:
    print(e-s+1)
else:
    print(0)


