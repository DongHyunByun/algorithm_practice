def heapify(unsorted, index, heap_size):
    smallist = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] < unsorted[smallist]:
        smallist = left_index
    if right_index < heap_size and unsorted[right_index] < unsorted[smallist]:
        smallist = right_index
    if smallist != index:
        unsorted[smallist], unsorted[index] = unsorted[index], unsorted[smallist]
        heapify(unsorted, smallist, heap_size)


def solution(scoville, K):
    n=len(scoville)
    #hepify
    for i in range(n//2-1,-1,-1):
        heapify(scoville,i,n)
    ans=0
    while (scoville[0]<K):
        if len(scoville)==1:
            return -1
    
        a=scoville[0]
        scoville[0]=scoville.pop()
        heapify(scoville,0,len(scoville))
        scoville[0]=a+scoville[0]*2
        heapify(scoville,0,len(scoville))
        
        ans+=1
    
    return ans