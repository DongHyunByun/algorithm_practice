def isPalindrome(word):
    for i in range(len(word)//2):
        if word[i]!=word[-(i+1)]:
            return False
    return True


for t in range(10):
    N=int(input())
    L=[]
    for i in range(8):
        L.append(input())
    ans=0

    for i in range(8):
        for j in range(9-N):
            if isPalindrome(L[i][j:j+N])==True:
                ans+=1

    for j in range(8):
        for i in range(9-N):
            if isPalindrome([a[j] for a in L[i:i+N]])==True:
                ans+=1
            

    print(f"#{t+1} {ans}")

    

