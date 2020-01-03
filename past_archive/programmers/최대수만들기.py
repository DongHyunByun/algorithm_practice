#문제 : https://chaibin0.tistory.com/entry/%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0


#n은 필요한수
def getnum(n,number):
    if n==len(number):
        return number
    else:
        tem=max(number[0:len(number)-n+1])
        del(number[0:number.index(tem)+1])
        return [tem]+getnum(n-1,number)

def solution(number,k):
    ans=''
    n=len(number)-k
    anslist=getnum(n,list(number))
    for i in anslist:
        ans+=i
    return ans
 


    
print(solution("1231234",3))