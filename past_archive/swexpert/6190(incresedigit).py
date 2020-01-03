
def isIncrease(n):
    '''
    문자열 n을주면 단조증가인지 판단
    '''
    for i in range(len(n)-1):
        if int(n[i])>int(n[i+1]):
            return False
    return True


def toMultiple(L):
    '''
    리스트를 주면 두개씩 조합의 곱을 list type으로 리턴
    '''
    multi=set()
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            multi.add(L[i]*L[j])
    return multi


for t in range(int(input())):
    maxmulti=0
    N=int(input())
    L=list(map(int,input().split()))
    MultiList=list(map(str,toMultiple(L)))
   

    for i in MultiList:
        if (isIncrease(i)==True) and (maxmulti<int(i)) :
            maxmulti=int(i)
    print(f"#{t+1} {maxmulti}")




