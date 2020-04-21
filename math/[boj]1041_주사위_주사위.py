import sys
N=int(input())
dice=list(map(int,input().split()))

if N==1:
    print(sum(dice)-max(dice))
    sys.exit()

def threeSum(a,b,c):
    return dice[a]+dice[b]+dice[c]
def twoSum(a,b):
    return dice[a]+dice[b]

#3면 최솟값
minThree=min([threeSum(3,4,5),threeSum(1,3,5),threeSum(0,1,3),threeSum(0,3,4),
              threeSum(0,2,4),threeSum(0,1,2),threeSum(1,2,5),threeSum(2,4,5)])
#2면 최솟값
twoL=[]
for i in range(6):
    for j in range(i+1,6):
        if i+j!=5:
            twoL.append(twoSum(i,j))
minTwo=min(twoL)
#1면 최솟값
minOne=min(dice)

numOne=(N-2)*(N-1)*4+(N-2)*(N-2)
numTwo=(N-1)*4+(N-2)*4
numThree=4
print(minOne*numOne+minTwo*numTwo+minThree*numThree)

