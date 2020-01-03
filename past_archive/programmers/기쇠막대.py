def solution(arrangement):
    isRazer=False
    totalStick=0
    stick=0
    
    for i in range(len(arrangement)-1):
        if arrangement[i]=="(":
            
            #레이저인경우
            if arrangement[i+1]==")":
                isRazer=True
                totalStick+=stick    
            #stick인경우
            else:
                stick+=1
                totalStick+=1
                
                
        else:
            if isRazer:
                isRazer=False
                continue
            else:
                stick-=1
        
        
    return totalStick

for t in range(int(input())):
    print(f"#{t+1} {solution(input())}")