#test case 1 오류

def dfs(city,ans,tickets,size,ansL):
    if (len(ans)==size):
            ansL.append(ans)
            ansL.sort()
            print(ansL)
            return
    for i in tickets:
        if ( (i[0]==city[1]) and (i not in ans) ):
            dfs(i,ans+[i],tickets,size,ansL)



def solution(tickets):
    size=len(tickets)
    ansL=[]
    startL=[]
    for i in tickets:
        if (i[0]=="ICN"):
            startL.append(i)
            
    #인천에서 첫 도착지 순으로 정렬
    startL.sort()

    for i in startL:
        dfs(i,[i],tickets,size,ansL)
        if ansL!=[]:
            finalAns=["ICN"]
            for i in ansL[0]:
                finalAns.extend([i[1]])
            
            return finalAns

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
