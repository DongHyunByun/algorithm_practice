N=input()
size=len(N)
ans=0
for i in range(1,size):
    ans+=9*pow(10,i-1)*i
print(ans+size*(int(N)-pow(10,(size-1))+1))