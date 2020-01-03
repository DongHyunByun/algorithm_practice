def dfs(city,ans,tickets,size,ansL):
    for i in tickets:
        if ( (i[0]==city[1]) and (i not in ans) ):
            ans.extend([i])
            if (len(ans)==size):
                ansL.append(ans)
                ansL.sort()
                print(ansL)
                return
            else:
                dfs(i,ans,tickets,size,ansL)



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
            


#dfs의 for문이 ans때문에 반복되지 않음.