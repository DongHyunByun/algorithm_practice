N,M=map(int,input().split())
pack=[]
each=[]
for i in range(M):
    p,e=map(int,input().split())
    pack.append(p)
    each.append(e)

lowPack=min(pack)
lowEach=min(each)

ans=min(N//6*lowPack+N%6*lowEach,(N//6+1)*lowPack,N*lowEach)
print(ans)

