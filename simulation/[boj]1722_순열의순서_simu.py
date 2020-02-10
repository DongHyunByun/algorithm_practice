import math

def fac(N):
    ans=1
    for i in range(1,N+1):
        ans*=i
    return ans

def main():
    N=int(input())
    L=list(map(int,input().split()))
    prob=L.pop(0)
    # 몇번째 수열?
    if prob==2:
        preL=[]
        ans=1
        for indx,num in enumerate(L):
            cnt=0
            for j in range(1,num):
                if not j in preL:
                    cnt+=1
            ans+=cnt*fac(N-1-indx)
            preL.append(num)
        print(ans)
    # 수열만들기
    else:
        K=L[0]-1
        ansL=[]
        allL=[i for i in range(1,N+1)]
        #i번째 숫자를 구하자
        for i in range(1,N+1):
            tempFac=fac(N-i)
            ansL.append(allL[K//tempFac])
            del allL[K//tempFac]
            K=K%tempFac
        print(*ansL)
main()

