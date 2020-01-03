
def isIncrease(n):
    '''
    문자열 n을주면 단조증가인지 판단
    '''
    if len(n)==1 :
        return False
    for i in range(len(n)-1):
        if int(n[i])>int(n[i+1]):
            return False
    return True

for t in range(int(input())):
    multiList=[]
    N=int(input())
    L=list(map(int,input().split()))

    for i in range(len(L)-1):
        for j in range(i+1,N):
            if isIncrease(str(L[i]*L[j]))==True:
                multiList.append(L[i]*L[j])
    maxi=max(multiList,default=-1)
    print(f"#{t+1} {maxi}")