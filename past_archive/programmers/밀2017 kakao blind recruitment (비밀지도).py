def solution(n,arr1,arr2):
    answer=[]

    for i in range(n):
        temp1=bin(arr1[i])[2:].zfill(n)
        temp2=bin(arr2[i])[2:].zfill(n)
        temp3=""
        for j in range(n):
            if (temp1[j]=="0" and temp2[j]=="0"):
                temp3+=" "
            else :
                temp3+="#"

        answer.append(temp3)

    return answer

    