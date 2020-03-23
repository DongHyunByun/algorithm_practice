import math

startDigit=["2","3","5","7"]
digit=["1","3","7","9"]

N=int(input())
def isPrime(number):
    if number==1:
        return False
    if number==2:
        return True
    if number%2==0:
        return False
    maxNum=int(math.sqrt(number))
    for i in range(3,maxNum,2):
        if number%i==0:
            return False
    return True

def dfs(num):
    if len(num)==N:
        print(num)
        return
    for d in digit:
        tempNum=num+d
        if isPrime(int(tempNum)):
            dfs(tempNum)

for i in startDigit:
    dfs(i)