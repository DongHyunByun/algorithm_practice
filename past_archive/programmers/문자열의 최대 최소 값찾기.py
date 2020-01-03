'''
빈칸으로 구분된 숫자로 이루어진 문자열의 최솟값과 최댓값을 리턴하는 함수
'''

def solution(s):
    i=0
    thisNStr=""
    while(s[i]!=" "):
        thisNStr += s[i]
        i+=1
        
    maxN=int(thisNStr)
    minN=int(thisNStr)
    i+=1
    
    while(i<=len(s)-1):
        thisNStr=""

        try :
            while(s[i]!=" "):
                thisNStr+=s[i]
                i+=1
        except:
            pass
            
        thisN=int(thisNStr)
        

        if thisN>maxN:
            maxN=thisN
        if thisN<minN:
            minN=thisN
        
        i+=1
    
    return str(minN)+' '+str(maxN)

print(solution("-3 -3 -5 -6 2 4 -340 2352 43 52 -6334"))