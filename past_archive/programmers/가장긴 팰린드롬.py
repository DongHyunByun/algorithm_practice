def isPalin(word):
    size=len(word)
    for i in range(size//2):
        if word[i]!=word[size-1-i]:
            return False
    return True

def solution(s):
    ans=1
    for i in range(len(s)):
        for j in range(len(s)-1,i,-1):
            if (j+1-i>ans and isPalin(s[i:j+1])):
                ans=j+1-i
    return ans