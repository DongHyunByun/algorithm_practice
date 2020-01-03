#solution(n,k) : 1~n의 숫자로 이루어진 list가 가능한 순열을 모두 나타내고 오름차순으로 정렬했을때 k번째 리스트를 반환하는

def recursive(L,tL,n):
    if len(L)==n:
        temL=list(L)
        tL.append(temL)
    else:
        for i in range(n):
            if i+1 in L:
                continue
            else:
                L.append(i+1)
                recursive(L,tL,n)
                L.pop()

def solution(n, k):
    totalList=[]
    mlist=[]
    recursive(mlist,totalList,n)
    totalList.sort()
    print(totalList)
    answer = totalList[k-1]
    return answer

print(solution(4,2))
