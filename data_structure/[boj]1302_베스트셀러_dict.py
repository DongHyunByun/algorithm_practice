N=int(input())
dict={}

for i in range(N):
    book=input()
    if book in dict:
        dict[book]+=1
    else:
        dict[book]=1

cnt=0
ans=[]
for key in dict:
    if cnt<dict[key]:
        ans=[key]
        cnt=dict[key]
    elif cnt==dict[key]:
        ans.append(key)

ans.sort()
print(ans[0])