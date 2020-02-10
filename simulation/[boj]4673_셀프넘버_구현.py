def fuc(n):
    num=n
    digitSum=0
    while(n!=0):
        digitSum+=n%10
        n=n//10
    return num+digitSum

# 0이면 selfNum
selfNum=[0 for i in range(10001)]
selfNum[0]=1

for i in range(1,10001):
    temp=fuc(i)
    if temp<=10000:
        selfNum[temp]=1

for i in range(1,10001):
    if selfNum[i]==0:
        print(i)