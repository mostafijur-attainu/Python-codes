# Merge Sort

def MergeSort(arr, st, en):

    if st >= en:
        return arr
   
    mid = (st+en)//2
    firsthalf = arr[st:mid+1]
    secondhalf = arr[mid+1:en+1]

    sortedfirst = MergeSort(firsthalf,0,len(firsthalf) - 1)
    sortedsecond = MergeSort(secondhalf, 0, len(secondhalf) - 1)
    
    # Merge 
    mergedarray = []
    
    i = 0
    j = 0

    while i< len(sortedfirst) and j < len(sortedsecond):

        if(sortedfirst[i] < sortedsecond[j]):
            mergedarray.append(sortedfirst[i])
            i = i+1
        else:
            mergedarray.append(sortedsecond[j])
            j = j+1
    
    while i < len(sortedfirst):
        mergedarray.append(sortedfirst[i])
        i = i+1
    
    while j < len(sortedsecond):
        mergedarray.append(sortedsecond[j])
        j = j+1
    
    return mergedarray
        
    

arr = [6,5,4,3,2,1]

print(MergeSort(arr,0,len(arr)-1))
